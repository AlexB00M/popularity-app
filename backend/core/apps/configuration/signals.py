from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PopularityConfig
from core.apps.user.models import User
from core.apps.items.starGift.models import StarGift
from core.apps.items.starGiftUnique.models import StarGiftUnique
from django.db.models import F
from core.apps.user.tasks import update_user_popularity_task

@receiver(post_save, sender=PopularityConfig)
def update_popularity_add_on_config_change(sender, instance, created, **kwargs):
    popularity_per_star = instance.popularity_per_star
    popularity_per_ton = instance.popularity_per_ton

    StarGift.objects.update(
        popularity_add=F('price') * popularity_per_star
    )

    StarGiftUnique.objects.update(
        popularity_add=F('average_price') * popularity_per_ton
    )

    for user in User.objects.all():
        update_user_popularity_task.delay(user.telegram_id)