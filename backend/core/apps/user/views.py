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
import requests
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.cache import cache
from core.apps.items.starGift.models import UserStarGift
from core.apps.items.starGiftUnique.models import UserStarGiftUnique
from core.apps.user.tasks import update_telegram_star_gifts, update_telegram_star_gifts_unique
from core.apps.items.starGift.serializers import StarGiftSerializer, UserStarGiftSerializer
from core.apps.items.starGiftUnique.serializers import StarGiftUniqueSerializer, UserStarGiftUniqueSerializer

#/api/auth/telegram/ POST
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
    
#/api/users/user_gifts/ GET
class UserGiftsView(APIView):
    permission_classes = [AllowAny] # Поменять IsAuthenticated
    
    def get(self, request):
        user = request.user
        print('aaaa')
        user_star_gifts = UserStarGift.objects.filter(user=user)
        user_star_gifts_unique = UserStarGiftUnique.objects.filter(user=user)
        
        serialized_gifts = UserStarGiftSerializer(user_star_gifts, many=True).data
        serialized_unique_gifts = UserStarGiftUniqueSerializer(user_star_gifts_unique, many=True).data

        print(serialized_gifts)
        print(serialized_unique_gifts)

        response = requests.get(
            f'{settings.TELEGRAM_API_URL}/user_gifts/pam',
            headers=settings.TELEGRAM_API_HEADERS
        )

        if response.status_code == 200:
            user_gifts_telegram = response.json()

            telegram_gifts = user_gifts_telegram["gifts"]
            telegram_unique_gifts = user_gifts_telegram["gifts_unique"]

            
        
        return Response("Обновление подарков запущено")
    
#/api/users/leaderboard/<page>/ GET
class LeaderboardView(APIView):
    permission_classes = [AllowAny] # Поменять IsAuthenticated

    def get(self, request, page):
        cache_key = f"leaderboard_page_{page}"
        cached_data = cache.get(cache_key)

        if cached_data is not None:
            print('Закешированную отдал')
            return Response(cached_data)
        else:
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

            data_for_cache = {
                "page": page,
                "total_pages": total_pages,
                "total_users": total_users,
                "data": data
            }
            cache.set(cache_key, data_for_cache, timeout=30) 

            return Response(data_for_cache)

#/api/users/user_rank/ GET
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