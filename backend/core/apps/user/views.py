from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from init_data_py import InitData
from django.conf import settings
from .models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer

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

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"message": f"Hello, {request.user}"})
