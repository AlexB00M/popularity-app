from django.db import models
from core.apps.items.emoji.models import Emoji
from core.apps.user.models import User
from django.core.exceptions import ValidationError

class Message(models.Model):
    id = models.AutoField(primary_key=True) 
    message_text = models.CharField(max_length=1024, blank=True)
    emojis = models.ManyToManyField(Emoji, related_name='messages')

    user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')

    def __str__(self):
        return str(self.id)
    
    def clean(self):
        if self.user_from == self.user_to:
            raise ValidationError("Нельзя отправить сообщение самому себе.")

    def save(self, *args, **kwargs):
        self.full_clean()  # Обеспечивает вызов clean() при сохранении
        super().save(*args, **kwargs)