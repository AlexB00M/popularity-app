from django.db import models
from core.apps.user.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal
from django.utils import timezone
from core.apps.items.message.models import Message

class StarGiftUnique(models.Model):
    # Gift data
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    popularity_add = models.PositiveIntegerField(blank=True, null=True)
    average_price = models.PositiveIntegerField(blank=True, null=True)
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
        verbose_name_plural = "StarGiftUnique"

    def __str__(self):
        return f"{self.title} {self.model}"

class UserStarGiftUnique(models.Model):
    # UserCard data
    id = models.BigIntegerField(primary_key=True)
    slug = models.CharField(max_length=100, blank=True, null=True) 
    num = models.PositiveIntegerField(blank=True, null=True)
    pattern = models.CharField(max_length=100, blank=True, null=True)
    backdrop = models.CharField(max_length=100, blank=True, null=True)

    received_date = models.DateTimeField(default=timezone.now)
    get_from_app = models.BooleanField(default=False)

    lottie_animation_json = models.JSONField(blank=True, null=True)
    lottie_animation_url = models.URLField(max_length=200, blank=True, null=True)

    # Сomparison with tables
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='star_gifts_unique')
    star_gift_unique = models.ForeignKey(StarGiftUnique, on_delete=models.CASCADE, related_name='star_gifts_unique')
    sender_id = models.BigIntegerField(blank=True, null=True)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='star_gift_messages', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Users StarGiftsUnique"

    def __str__(self):
        return f'{self.user.user_name} — {self.slug} | {self.star_gift_unique.title} {self.star_gift_unique.model} {self.pattern} {self.backdrop}'