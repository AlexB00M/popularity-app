from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from core.apps.user.tasks import update_user_popularity_task , update_star_gift_popularity_add_task
from .models import UserStarGift, StarGift

@receiver([post_save, post_delete], sender=UserStarGift)
def update_user_popularity_from_gift(sender, instance, created=None, **kwargs):
    update_user_popularity_task.delay(instance.user.telegram_id)

@receiver([post_save, post_delete], sender=StarGift)
def recalculate_popularity_add(sender, instance, created=None, **kwargs):
    update_star_gift_popularity_add_task.delay(instance.id)