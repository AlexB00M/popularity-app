from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from init_data_py import InitData
from django.conf import settings
from .models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserSerializer, UserLeaderboardSerializer
from rest_framework.exceptions import NotFound
import math
import requests
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.cache import cache
from core.apps.items.starGift.models import UserStarGift, StarGift
from core.apps.items.starGiftUnique.models import UserStarGiftUnique, StarGiftUnique 
from core.apps.user.tasks import update_telegram_star_gifts_task, update_telegram_star_gifts_unique_task, update_user_star_gifts_info, update_user_star_gifts_unique_info
from core.apps.items.starGift.serializers import StarGiftSerializer, UserStarGiftSerializer
from core.apps.items.starGiftUnique.serializers import StarGiftUniqueSerializer, UserStarGiftUniqueSerializer
from core.apps.items.message.models import Message
from core.apps.exception.models import LoggedException
from core.apps.giftsLogs.models import GiftLog
from datetime import datetime
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.db.models import Q

#/api/auth/telegram/ POST
class TelegramTokenView(APIView):
    permission_classes = [AllowAny] 

    def post(self, request):
        query_string = request.data.get('initData')
        if not query_string:
            return Response({"detail": "initData is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        init_data = InitData.parse(query_string)
        is_valid = init_data.validate(
            bot_token=settings.TELEGRAM_BOT_TOKEN,
            lifetime=3600,
        )
        if is_valid:
            user = self.get_or_create_user(init_data)
            tokens = self.create_tokens(user)
            return Response({'tokens': tokens, 'user': UserSerializer(user).data})
        else:
            return Response({"detail": "Invalid initData"}, status=status.HTTP_400_BAD_REQUEST)
    
    def get_or_create_user(self, init_data):
        user_data = init_data.user
        user, created = User.objects.get_or_create(
            telegram_id = user_data.id,
            defaults={
                'user_name': user_data.username,
                'first_name': user_data.first_name,
                'last_name': user_data.last_name,
                'photo_url': user_data.photo_url,
            }
        )
        return user

    def create_tokens(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }
import time
import json


#/api/users/user_gifts/ GET
class UserGiftsView(APIView):
    permission_classes = [AllowAny] # Поменять IsAuthenticated
    
    def get(self, request):
        with open('core/apps/user/user_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f) 
        #user = request.user
        start = time.perf_counter()

        user = User.objects.get(telegram_id=5000549728)
        telegram_id = user.telegram_id

        key = f"usercache:{request.user.id}"
        response = cache.get(key)

        if response:
            print('отдал кэш')
            return Response(response)
        start = time.perf_counter()
        try:
            response_telegram_api = requests.get(
                f'{settings.TELEGRAM_API_URL}/user_gifts/cKUMhedgehog',
                headers=settings.TELEGRAM_API_HEADERS
            )
        except Exception as e:
            LoggedException.objects.create(
                text=str(e),
                user=user
            )
            print(e)
            return Response("Ошибкуа получения данных")
        
        response_telegram_api_data = data#response_telegram_api.json()
        user_star_gifts_telegram = response_telegram_api_data['gifts']
        user_star_gifts_telegram_unique = response_telegram_api_data['gifts_unique']

        response_data = {"gifts": [], "gifts_unique": [], "gifts_animations": {}}

        update_user_star_gifts_info.delay(user_star_gifts_telegram, telegram_id)
        # update_user_star_gifts_unique_info.delay(user_star_gifts_telegram_unique, telegram_id)

        # StarGift
        user_star_gifts_telegram_ids = set(gift["id"] for gift in user_star_gifts_telegram)
        star_gifts = StarGift.objects.filter(id__in=user_star_gifts_telegram_ids)
        star_gifts = {star_gift.id:star_gift for star_gift in star_gifts}

        for user_star_gift in user_star_gifts_telegram:
            id = user_star_gift["id"]
            if id in star_gifts:
                response_data["gifts"].append({
                    "id": id,
                    "name": star_gifts[id].name,
                    "popularity_add": star_gifts[id].popularity_add,
                    "received_date": timezone.make_aware(datetime.fromtimestamp(user_star_gift["received_date"])).strftime('%Y-%m-%d %H:%M:%S'),
                })

        # StarGiftUnique 

        filters = [{"model": gift["model"], "title": gift["title"]} for gift in user_star_gifts_telegram_unique]
        query = Q()
        for f in filters:
            query |= Q(model=f['model'], title=f['title'])
        star_gifts_unique = StarGiftUnique.objects.filter(query)
        star_gifts_unique = {(star_gift_unique.model, star_gift_unique.title): star_gift_unique for star_gift_unique in star_gifts_unique}
        user_star_gifts_unique = user.star_gifts_unique.all()
        user_star_gifts_unique = {user_star_gift_unique.id:user_star_gift_unique for user_star_gift_unique in user_star_gifts_unique}

        star_gift_unique_to_create = {}

        for user_star_gift_telegram_unique in user_star_gifts_telegram_unique:
            id = user_star_gift_telegram_unique["id"]
            model = user_star_gift_telegram_unique["model"]
            title = user_star_gift_telegram_unique["title"]
            template = (model, title)
            response_template = {
                "id": id,
                "title": title,
                "model": model,
                "slug": user_star_gift_telegram_unique["slug"],
                "pattern": "",
                "backdrop": "",
                "average_price": "",
                "popularity_add": "",
                "received_date": "",
                "lottie_animation_json": "",
            }
            if template in star_gifts_unique:
                star_gift_unique = star_gifts_unique.get(template)
                response_template["average_price"] = star_gift_unique.average_price
                response_template["popularity_add"] = star_gift_unique.popularity_add
                if id in user_star_gifts_unique:
                    user_star_gift_unique = user_star_gifts_unique.get(id)
                    response_template["pattern"] = user_star_gift_unique.pattern
                    response_template["backdrop"] = user_star_gift_unique.backdrop
                    response_template["received_date"] = user_star_gift_unique.received_date.strftime('%Y-%m-%d %H:%M:%S')
                    response_template["lottie_animation_json"] = user_star_gift_unique.lottie_animation_json
                    response_template["sender_id"] = user_star_gift_unique.sender_id or None
                else:
                    print(star_gift_unique)
                    payload = [{
                        "title" : user_star_gift_telegram_unique["title"],
                        "slug": user_star_gift_telegram_unique["slug"],
                        "average_price": 1
                    }]
                    try:
                        response_telegram_api = requests.post(
                            f'{settings.TELEGRAM_API_URL}/get_more_info_unique_gifts',
                            headers=settings.TELEGRAM_API_HEADERS,
                            json=payload
                        )
                        response_telegram_api = response_telegram_api.json()
                        lottie_animation_json = response_telegram_api[0]["lottie_animation_json"]
                        pattern = response_telegram_api[0]["pattern"]
                        backdrop = response_telegram_api[0]["backdrop"]
                        
                        sender_id = response_telegram_api[0].get("sender_id")
                        if sender_id:
                            response_template["sender_id"] = sender_id

                        response_template["pattern"] = pattern
                        response_template["backdrop"] = backdrop
                        response_template["received_date"] = timezone.make_aware(datetime.fromtimestamp(user_star_gift_telegram_unique["received_date"])).strftime('%Y-%m-%d %H:%M:%S')
                        response_template["lottie_animation_json"] = lottie_animation_json

                        star_gift_unique_to_create[id] = response_template
                        print("Получил анимацию")

                    except Exception as e:
                        LoggedException.objects.create(
                            text=str(e),
                            user=user
                        )
                    response_data["gifts_unique"].append(response_template)
            else:
               GiftLog.objects.create(
                   text=f"StarGiftUnique {model} {title} not in base"
               ) 

        update_user_star_gifts_unique_info.delay(user_star_gifts_telegram_unique, star_gift_unique_to_create, telegram_id)

        # end = time.perf_counter()
        # print(f"Время выполнения: {end - start:.4f} секунд")

        # cache.set(key, response_data, 5)

        return Response(response_data)

    
#/api/users/leaderboard/<page>/ GET
class LeaderboardView(APIView):
    permission_classes = [AllowAny] # Поменять IsAuthenticated

    def get(self, request, page):
        limit = 50
        total_users = User.objects.count()
        total_pages = math.ceil(total_users / limit)

        if page < 1 or page > total_pages:
            raise NotFound(f"Страница {page} не существует. Доступные страницы: 1 - {total_pages}")

        offset = (page - 1) * limit
        users = User.objects.order_by("-total_popularity")[offset:offset + limit]
        serializer = UserLeaderboardSerializer(users, many=True)

        data = []
        start_rank = offset + 1
        for i, user_data in enumerate(serializer.data):
            user_data['rank'] = start_rank + i
            data.append(user_data)

        data_for_cache = {
            "page": page,
            "total_pages": total_pages,
            "total_users": total_users,
            "data": data
        }

        return Response(data_for_cache)

#/api/users/user_rank/ GET
class UserRankView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = request.user
        except User.DoesNotExist:
            return Response({"detail": "Пользователь не найден."}, status=status.HTTP_404_NOT_FOUND)

        higher_count = User.objects.filter(total_popularity__gt=user.total_popularity).count()
        rank = higher_count + 1

        return Response({
            "rank": rank,
            "total_popularity": user.total_popularity
        })