from celery import shared_task
from core.apps.user.models import User
from core.apps.user.services import calculate_user_popularity  
import requests
from django.conf import settings
from core.apps.items.starGift.models import StarGift, UserStarGift
from core.apps.items.starGiftUnique.models import UserStarGiftUnique, StarGiftUnique
from core.apps.configuration.models import PopularityConfig
from django.db.models import F, Q
from .serializers import UserSerializer
from core.apps.giftsLogs.models import GiftLog
from datetime import datetime
from django.utils import timezone
from core.apps.exception.models import LoggedException

@shared_task
def update_user_popularity_task(telegram_id):
    try:
        calculate_user_popularity(telegram_id)
        return f'Обновление популярности пользователя с telegram_id={telegram_id} завершено'
    except User.DoesNotExist:
        return f"Пользователь {telegram_id} не найден (update_user_popularity_task)"


@shared_task(max_retries=0)
def update_telegram_star_gifts_task(targets):
    try:
        response = requests.get(
            f'{settings.TELEGRAM_API_URL}/get_telegram_gifts',
            headers=settings.TELEGRAM_API_HEADERS,
        )
        data = response.json()
        ids = [gift.id for gift in data]
        for target in targets:
            id = target["id"]
            if id in ids:
                item = next((i for i in data if i["id"] == id), None)
                gift, created = StarGift.objects.get_or_create(
                    id=item["id"],
                    defaults={
                        'lottie_animation_json': item['lottie_animation_json']['data'], 
                        'price': item['price'], 
                        'convert_stars': item['convert_stars'], 
                        'sold_out': item['sold_out']
                    }
                )
                if created:
                    GiftLog.objects.create(
                        text=f"Gift created",
                        star_gift=gift
                    )
            else:
                GiftLog.objects.create(
                    text=f"Gift not found in telegram id: {id}",
                )
        return f'Обновление подарков starGifts завершено'        
    except Exception as e:
        return str(e)


@shared_task(max_retries=0)
def update_telegram_star_gifts_unique_task(targets):

    try:
        for target in targets:
            payload = {
                "title" : target["title"],
                "model": target["model"], 
            }
            response = requests.post(
                f'{settings.TELEGRAM_API_URL}/unique_gift_average_price',
                headers=settings.TELEGRAM_API_HEADERS,
                json=payload
            )
            data = response.json()
            gift_unique = StarGiftUnique.objects.get(title=target["title"], model=target["model"])
            if isinstance(data, float):
                gift_unique.average_price = data
                gift_unique.save()
            else:
                GiftLog.objects.create(
                    text=data,
                    star_gift_unique=gift_unique
                )
        return f'Обновление подарков starGiftsUnique завершено'
    except User.DoesNotExist:
        return f"Ошибка обновления подарков starGifts"

@shared_task
def update_star_gift_popularity_add_task(gift_id):
    try:
        config = PopularityConfig.objects.get(name='Конфигурация популярности за ценность')
        popularity_per_star = config.popularity_per_star

        StarGift.objects.filter(id=gift_id).update(
            popularity_add=F('price') * popularity_per_star
        )
        gift = StarGift.objects.get(id=gift_id)
        user_ids = gift.user_star_gifts.values_list('user__telegram_id', flat=True)

        for user_id in user_ids:
            update_user_popularity_task.delay(user_id)

        return f'Обновил popularity_add для {gift_id} StarGift | users: {user_ids}'
    
    except StarGift.DoesNotExist:
        return f"Ошибка update_star_gift_popularity_add_task"

@shared_task
def update_star_gift_unique_popularity_add_task(gift_id):
    try:
        config = PopularityConfig.objects.get(name='Конфигурация популярности за ценность')
        popularity_per_ton = config.popularity_per_ton

        StarGiftUnique.objects.filter(id=gift_id).update(
            popularity_add=F('average_price') * popularity_per_ton
        )
            
        try:
            user_star_gift_unique = UserStarGiftUnique.objects.get(star_gift_unique__id=gift_id)
            user_id = user_star_gift_unique.user.telegram_id

            if user_id:
                update_user_popularity_task.delay(user_id)

            return f'Обновил popularity_add для {user_star_gift_unique.slug} StarGiftUnique | user: {user_id}'
        
        except UserStarGiftUnique.DoesNotExist:
            return f"Нету пользователя с этим подарком id:{gift_id}"
    except StarGiftUnique.DoesNotExist:
        return f"Ошибка update_star_gift_unique_popularity_add_task"



@shared_task
def update_user_star_gifts_info(user_star_gifts_telegram, telegram_id):
    user = User.objects.get(telegram_id=telegram_id)

    gifts_to_add_received_dates = []
    gifts_to_dell_received_dates = []

    user_star_gifts_telegram = {gift["received_date"]:gift for gift in user_star_gifts_telegram}
    user_star_gifts = UserStarGift.objects.filter(user=user)
    user_star_gifts_received_dates = {}

    star_gifts = StarGift.objects.all()
    star_gifts = {gift.id:gift for gift in star_gifts}

    for gift in user_star_gifts:
        received_date = int(gift.received_date.timestamp())
        user_star_gifts_received_dates[received_date] = gift
        gifts_to_dell_received_dates.append(received_date)

    for user_star_gift_telegram in user_star_gifts_telegram:
        gift_id = user_star_gifts_telegram[user_star_gift_telegram]["id"]
        if gift_id not in star_gifts:
            GiftLog.objects.create(
                text=f"No StarGift in base {gift_id}",
            )
        else:
            if user_star_gift_telegram not in user_star_gifts_received_dates:
                gifts_to_add_received_dates.append(user_star_gift_telegram)
            else:
                gifts_to_dell_received_dates.remove(user_star_gift_telegram)

    gifts_to_dell_received_dates = [timezone.make_aware(datetime.fromtimestamp(ts)) for ts in gifts_to_dell_received_dates]
    
    UserStarGift.objects.filter(received_date__in=gifts_to_dell_received_dates).delete()
    gifts_to_create = [
        UserStarGift(
            user=user,
            star_gift=star_gifts[user_star_gifts_telegram[received_date]["id"]],
            received_date=timezone.make_aware(datetime.fromtimestamp(received_date)),
            sender_id=user_star_gifts_telegram[received_date]["sender_id"]
        )
        for received_date in gifts_to_add_received_dates
    ]
    UserStarGift.objects.bulk_create(gifts_to_create)

@shared_task
def update_user_star_gifts_unique_info(user_star_gifts_telegram_unique, star_gifts_unique_to_create, telegram_id):
    # star_gift_unique_targets_avg_price = []

    user = User.objects.get(telegram_id=telegram_id)
    user_star_gifts_telegram_unique = {gift["id"]: gift for gift in user_star_gifts_telegram_unique}

    star_gifts_unique = StarGiftUnique.objects.all()
    star_gifts_unique = {(star_gift_unique.model, star_gift_unique.title): star_gift_unique for star_gift_unique in star_gifts_unique}

    gifts_to_dell = []

    user_star_gitfts_unique = UserStarGiftUnique.objects.filter(user=user)
    user_star_gitfts_unique_dict = {}
    
    for user_star_gift_unique in user_star_gitfts_unique:
        id = user_star_gift_unique.id
        user_star_gitfts_unique_dict[id] = user_star_gift_unique
        gifts_to_dell.append(id)

    for user_star_gift_telegram_unique in user_star_gifts_telegram_unique:
        id = user_star_gift_telegram_unique
        model = user_star_gifts_telegram_unique[id]["model"]
        title = user_star_gifts_telegram_unique[id]["title"]
        template = (model, title)
        if template in star_gifts_unique:
                if id in gifts_to_dell:
                    gifts_to_dell.remove(id)
        else:
            GiftLog.objects.create(
                text=f"No StarGiftUnique in base {id} {model} {title}",
            )

    print(gifts_to_dell)

    print(star_gifts_unique_to_create)

    print(len(star_gifts_unique_to_create))

    UserStarGiftUnique.objects.filter(id__in=gifts_to_dell).delete()

    new_gifts = []

    for gift_data in star_gifts_unique_to_create.values():
        model = gift_data["model"]
        title = gift_data["title"]
        template = (model, title)

        star_gift_unique = star_gifts_unique.get(template)

        new_gifts.append(UserStarGiftUnique(
            id=gift_data["id"],
            user=user,
            star_gift_unique=star_gift_unique,
            pattern=gift_data["pattern"],
            backdrop=gift_data["backdrop"],
            sender_id=gift_data.get("sender_id"),  
            lottie_animation_json=gift_data["lottie_animation_json"],
            received_date=timezone.make_aware(datetime.strptime(gift_data["received_date"], '%Y-%m-%d %H:%M:%S'))
        ))

    UserStarGiftUnique.objects.bulk_create(new_gifts, batch_size=100)
    # update_telegram_star_gifts_unique_task.delay(star_gift_unique_targets_avg_price)