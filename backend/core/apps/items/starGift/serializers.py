from rest_framework import serializers
from .models import StarGift, UserStarGift


class StarGiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = StarGift
        fields = ("id")

class UserStarGiftSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    class Meta:
        model = UserStarGift
        fields = ("star_gift", "user", "user_name", "sender_id", "received_date", "get_from_app")

    def get_user_name(self, obj):
        return obj.user.user_name