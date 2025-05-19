from django.db import models
from core.apps.user.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal
from django.utils import timezone
from django.core.exceptions import ValidationError

class StarGift(models.Model):
    # Gift data
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    lottie_animation_json = models.JSONField(blank=True, null=True)  # Сюда загружается JSON-анимация Lottie
    lottie_animation_url = models.URLField(max_length=200, blank=True, null=True)
    popularity_add = models.PositiveIntegerField(blank=False, null=False)
    price = models.PositiveIntegerField(blank=False, null=False)
    convert_stars = models.PositiveIntegerField(blank=True, null=True)
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

    class Meta:
        verbose_name_plural = "StarGift"

    def __str__(self):
        return str(self.id)

class UserStarGift(models.Model):
    # UserCard data
    received_date = models.DateTimeField(default=timezone.now)
    get_from_app = models.BooleanField(default=False)

    # Сomparison with tables
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_star_gifts')
    star_gift = models.ForeignKey(StarGift, on_delete=models.CASCADE,  related_name='received_by_users')
    sender_id = models.BigIntegerField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Users StarGifts"

    def __str__(self):
        return f'{self.user.user_name} — {self.star_gift.id}'
    def clean(self):
        if self.sender_id and self.user == self.sender_id:
            raise ValidationError("Пользователь не может отправить подарок сам себе.")