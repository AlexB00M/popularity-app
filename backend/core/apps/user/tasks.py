from celery import shared_task
from core.apps.user.models import User
from core.apps.user.services import calculate_user_popularity  

@shared_task
def update_user_popularity_task(telegram_id):
    try:
        calculate_user_popularity(telegram_id)
    except User.DoesNotExist:
        return f"Пользователь {telegram_id} не найден"
