from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from core.apps.user.tasks import update_star_gift_unique_popularity_add_task, update_user_popularity_task
from .models import UserStarGiftUnique, StarGiftUnique

@receiver([post_save, post_delete], sender=UserStarGiftUnique)
def update_user_popularity_from_gift(sender, instance, created=None, **kwargs):
    old_instance = sender.objects.filter(pk=instance.pk).first()
    if old_instance and old_instance.lottie_animation_json != instance.lottie_animation_json:
        return
    update_user_popularity_task.delay(instance.user.telegram_id)

@receiver([post_save, post_delete], sender=StarGiftUnique)
def recalculate_popularity_add(sender, instance, created=None, **kwargs):
    update_star_gift_unique_popularity_add_task.delay(instance.id)