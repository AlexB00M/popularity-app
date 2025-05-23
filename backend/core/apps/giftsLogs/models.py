from django.db import models
from core.apps.items.starGift.models import StarGift, UserStarGift
from core.apps.items.starGiftUnique.models import StarGiftUnique, UserStarGiftUnique

class GiftLog(models.Model):
    # Gift data
    id = models.AutoField(primary_key=True)  
    timestamp = models.TimeField(auto_now=True)
    text = models.CharField(max_length=500, blank=True, null=True)

    star_gift = models.ForeignKey(StarGift, on_delete=models.SET_NULL, blank=True, null=True)
    star_gift_unique = models.ForeignKey(StarGiftUnique, on_delete=models.SET_NULL, blank=True, null=True)
    
    user_star_gift = models.ForeignKey(UserStarGift, on_delete=models.SET_NULL, blank=True, null=True)
    user_star_gift_unique = models.ForeignKey(UserStarGiftUnique, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f"{str(self.id)} {self.star_gift if self.star_gift else ''}{self.star_gift_unique if self.star_gift_unique else ''} - {self.text}"