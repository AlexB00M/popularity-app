from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
import requests
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class UpdateStarGiftsTelegramAdminView(APIView):
    permission_classes = [IsAdminUser]
    
    def get(self, request):
        user_gifts = requests.get(f'{settings.TELEGRAM_API_URL}/user_gifts/pambolovl', headers=settings.TELEGRAM_API_HEADERS)
        
        return Response(user_gifts) 