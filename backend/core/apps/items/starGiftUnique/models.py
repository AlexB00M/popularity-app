from django.db import models
from core.apps.user.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal
from django.utils import timezone
from core.apps.items.message.models import Message

class StarGiftUnique(models.Model):
    # Gift data
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    popularity_add = models.PositiveIntegerField(blank=False, null=False)
    average_price = models.PositiveIntegerField(blank=False, null=False) 
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
    slug = models.CharField(max_length=100) 
    num = models.PositiveIntegerField()
    pattern = models.CharField(max_length=100)
    backdrop = models.CharField(max_length=100)

    received_date = models.DateTimeField(default=timezone.now)
    get_from_app = models.BooleanField(default=False)

    lottie_animation_json = models.JSONField() 
    lottie_animation_url = models.URLField(max_length=200, blank=True, null=True)

    # Сomparison with tables
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='star_gift_unique')
    star_gift_unique = models.OneToOneField(StarGiftUnique, on_delete=models.CASCADE, related_name='user')
    sender_id = models.BigIntegerField(blank=True, null=True)
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='star_gift_messages', blank=True, null=True)

    class Meta:
        verbose_name_plural = "Users StarGiftsUnique"
        unique_together = ('user', 'star_gift_unique') 

    def __str__(self):
        return f'{self.user.user_name} — {self.slug} | {self.star_gift_unique.title} {self.star_gift_unique.model} {self.pattern} {self.backdrop}'