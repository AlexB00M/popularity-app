from django.db import models
from core.apps.user.models import User
from core.apps.items.card.models import Card
from core.apps.items.starGift.models import StarGift
from django.core.exceptions import ValidationError

class Roulette(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    cards = models.ManyToManyField(Card, related_name='roulettes_contain', blank=True)
    gifts = models.ManyToManyField(StarGift, related_name='roulettes_contain', blank=True)
    
    def __str__(self):
        return self.name

class RouletteSpin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='roulette_spins')
    roulette = models.ForeignKey(Roulette, on_delete=models.CASCADE, related_name='spins')
    timestamp = models.DateTimeField(auto_now_add=True)

    prize_card = models.ForeignKey(Card, on_delete=models.SET_NULL, null=True, blank=True)
    prize_gift = models.ForeignKey(StarGift, on_delete=models.SET_NULL, null=True, blank=True)

    
    def clean(self):
        if bool(self.prize_card) == bool(self.prize_gift):
            raise ValidationError("Должно быть заполнено только одно из полей: prize_card или prize_gift.")

    def save(self, *args, **kwargs):
        self.full_clean()  # Запускаем валидацию
        super().save(*args, **kwargs)

    def __str__(self):
        prize = self.card.name if self.card else (self.gift.name if self.gift else "No prize")
        return f'Spin by {self.user.user_name} on {self.roulette.name} — {prize} at {self.timestamp}'