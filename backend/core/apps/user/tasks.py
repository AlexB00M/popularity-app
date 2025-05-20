from celery import shared_task
from core.apps.user.models import User
from core.apps.user.services import calculate_user_popularity  
import requests
from django.conf import settings
from core.apps.items.starGift.models import UserStarGift, StarGift
from core.apps.items.starGiftUnique.models import UserStarGiftUnique, StarGiftUnique
from core.apps.configuration.models import PopularityConfig

@shared_task
def update_user_popularity_task(telegram_id):
    try:
        calculate_user_popularity(telegram_id)
        return f'Обновление популярности пользователя с telegram_id-{telegram_id} завершено'
    except User.DoesNotExist:
        return f"Пользователь {telegram_id} не найден"

@shared_task(bind=True, max_retries=0)
def update_telegram_star_gifts(user, gifts_to_check):
    try:
        
        return f""
    except User.DoesNotExist:
        return f"Пользователь с id={user.telegram_id} не найден"
    except Exception as e:
        return str(e)


@shared_task(bind=True, max_retries=0)
def update_telegram_star_gifts_unique(user, gifts_unique_not_in_base):
    try:
        response = requests.get(f'{settings.TELEGRAM_API_URL}/get_telegram_gifts', headers=settings.TELEGRAM_API_HEADERS)
        if response.status_code == 200:
            pass
        else:
            raise Exception(f'Ошибка обновления: {response.status_code} - {response.text}')

        return f'Обновление подарков starGifts завершено'
    except User.DoesNotExist:
        return f"Ошибка обновления подарков starGifts"

@shared_task
def recalculate_popularity_add_task(gift_id):
    config = PopularityConfig.objects.get(name='Конфигурация популярности за ценность')
    instance = StarGift.objects.get(id=gift_id)
    if isinstance(instance, StarGift):
        instance.popularity_add = config.popularity_per_star * instance.price
    elif isinstance(instance, StarGiftUnique):
        instance.popularity_add = config.popularity_per_star * instance.average_price

    users = [user_star_gift.user for user_star_gift in instance.users.all()]

    for user in users:
        calculate_user_popularity(user.id)

    return f"Пересчитал popularity_add для gift {instance.id} {instance.name if instance.name else ''}"