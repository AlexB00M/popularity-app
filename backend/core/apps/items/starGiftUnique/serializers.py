from rest_framework import serializers
from .models import StarGiftUnique, UserStarGiftUnique


class StarGiftUniqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarGiftUnique
        fields = ("id", "title", "model", "average_price")

class UserStarGiftUniqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStarGiftUnique
        fields = '__all__' 