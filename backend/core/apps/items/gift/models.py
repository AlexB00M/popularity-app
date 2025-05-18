from django.db import models
from core.apps.user.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal
from django.utils import timezone
from django.core.exceptions import ValidationError

class Gift(models.Model):
    # Gift data
    name = models.CharField(max_length=100, unique=True)
    lottie_animation_json = models.JSONField(blank=True, null=True)  # Сюда загружается JSON-анимация Lottie
    lottie_animation_url = models.URLField(max_length=200, blank=True, null=True)
    popularity_add = models.PositiveIntegerField(blank=False, null=False)
    price = models.PositiveIntegerField(blank=False, null=False) 
    drop_chance = models.DecimalField(
        max_digits=9, 
        decimal_places=6, 
        validators=[
            MinValueValidator(Decimal('0.000001')), 
            MaxValueValidator(Decimal('100.000000')) 
        ],
        null=True,
        blank=True
    )
    levels = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name

class UserGift(models.Model):
    # UserCard data
    timestamp = models.DateTimeField(default=timezone.now)
    get_from_app = models.BooleanField(default=True)

    # Сomparison with tables
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='gifts_received')
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE)
    sender_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Users Gifts"

    def __str__(self):
        return f'{self.user.user_name} — {self.gift.name}'
    def clean(self):
        if self.user_sender and self.user == self.user_sender:
            raise ValidationError("Пользователь не может отправить подарок сам себе.")