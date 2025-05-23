from rest_framework import serializers
from .models import Message
from core.apps.items.emoji.serializers import EmojiSerializer


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ("id", "title", "model", "average_price")