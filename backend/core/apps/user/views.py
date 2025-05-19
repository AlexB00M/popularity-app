from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from init_data_py import InitData
from django.conf import settings
from .models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer, UserLeaderboardSerializer
from rest_framework.exceptions import NotFound
import math
from rest_framework_simplejwt.authentication import JWTAuthentication
import requests
from rest_framework_simplejwt.tokens import RefreshToken

class TelegramTokenView(APIView):
    permission_classes = [AllowAny] 

    def post(self, request):
        query_string = request.data.get('initData')
        if not query_string:
            return Response({"detail": "initData is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        init_data = InitData.parse(query_string)
        is_valid = init_data.validate(
            bot_token=settings.TELEGRAM_BOT_TOKEN,
            lifetime=3600,
        )
        if is_valid:
            user = self.get_or_create_user(init_data)
            tokens = self.create_tokens(user)
            return Response({'tokens': tokens, 'user': UserSerializer(user).data})
        else:
            return Response({"detail": "Invalid initData"}, status=status.HTTP_400_BAD_REQUEST)
    
    def get_or_create_user(self, init_data):
        user_data = init_data.user
        user, created = User.objects.get_or_create(
            telegram_id = user_data.id,
            defaults={
                'user_name': user_data.username,
                'first_name': user_data.first_name,
                'last_name': user_data.last_name,
                'photo_url': user_data.photo_url,
            }
        )
        return user

    def create_tokens(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class UserGiftsView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        
        user_name = user.user_name
        user_gifts = requests.get(f'{settings.TELEGRAM_API_URL}/user_gifts/pambolovl', headers=settings.TELEGRAM_API_HEADERS)

        return Response(user_gifts) 

class LeaderboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, page):
        limit = 50

        total_users = User.objects.count()
        total_pages = math.ceil(total_users / limit)

        if page < 1 or page > total_pages:
            raise NotFound(f"Страница {page} не существует. Доступные страницы: 1 - {total_pages}")

        offset = (page - 1) * limit
        users = User.objects.order_by("-total_popularity")[offset:offset + limit]
        serializer = UserLeaderboardSerializer(users, many=True)
        
        data = []
        start_rank = offset + 1
        for i, user_data in enumerate(serializer.data):
            user_data['rank'] = start_rank + i
            data.append(user_data)

        return Response({
            "page": page,
            "total_pages": total_pages,
            "total_users": total_users,
            "data": data
        })

class UserRankView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = request.user
        except User.DoesNotExist:
            return Response({"detail": "Пользователь не найден."}, status=status.HTTP_404_NOT_FOUND)

        higher_count = User.objects.filter(total_popularity__gt=user.total_popularity).count()
        rank = higher_count + 1

        return Response({
            "rank": rank,
            "total_popularity": user.total_popularity
        })