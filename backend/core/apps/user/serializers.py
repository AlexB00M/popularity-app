from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserLeaderboardSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("telegram_id", "user_name", "total_popularity", "photo_url")