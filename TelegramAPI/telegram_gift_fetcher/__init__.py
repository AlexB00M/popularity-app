import asyncio
from telethon import functions
from typing import Optional, Dict
from telethon import TelegramClient
from telethon.tl.types import InputUser
from .tl_objects import GetUserStarGifts
from .scraper import get_unique_gift_average_price

async def _resolve_username(client: TelegramClient, username: str) -> Optional[tuple]:
    """
    Resolve a Telegram username to user ID and access hash.

    Args:
        client (TelegramClient): The Telegram client instance.
        username (str): The username to resolve.

    Returns:
        tuple or None: (user_id, access_hash) if resolved, None otherwise.
    """
    from telethon.tl.functions import contacts
    response = await client(contacts.ResolveUsernameRequest(username=username))
    if not response.users:
        print(f"No user found for username '{username}'")
        return None
    user = response.users[0]
    return user.id, user.access_hash


async def get_user_gifts(client: TelegramClient, username: str, offset: str = "", limit: int = 10) -> Dict:
    """
    Fetch gifts for a Telegram user using an existing client instance.

    Args:
        client (TelegramClient): An initialized and started TelegramClient instance.
        username (str): The target user's Telegram username.
        offset (str, optional): Offset for pagination. Defaults to "". Use as "5"/"50"/"100"
        limit (int, optional): Number of gifts to fetch. Defaults to 100.

    Returns:
        dict: Contains 'gifts' (list), 'count_gifts' (int), and 'total_cost' (dict with 'ton' and 'stars').
    """
    user_data = await _resolve_username(client, username)
    if user_data is None:
        return {'gifts': [], 'count_gifts': 0, 'total_cost': {'ton': 0.0, 'stars': 0}}
    user_id, access_hash = user_data
    user = InputUser(user_id=user_id, access_hash=access_hash)
    request = GetUserStarGifts(user_id=user, offset=offset, limit=limit)
    response = await client(request)

    # print("Общее количество подарков:", response.count)

    # for user_gift in response.gifts:
    #     print("--- Подарок ---")
    #     print("Тип подарка:", user_gift.gift.__class__.__name__)
    #     print("Дата получения:", user_gift.date)
    #     print("ID сообщения:", user_gift.msg_id)
    #     print("Скрыто ли имя отправителя:", user_gift.name_hidden)
    #     print("Отправитель:", user_gift.from_id)
    #     print("Текст сообщения:", user_gift.message)
        
    #     # Вложенный подарок
    #     gift = user_gift.gift
    #     print("ID подарка:", gift.id)

    #     if gift.CONSTRUCTOR_ID == 0x5c62d151:  # StarGiftUnique
    #         print("Название:", gift.title)
    #         print("Slug:", gift.slug)
    #         print("Выпущено:", gift.availability_issued)
    #         print("Всего:", gift.availability_total)
    #     elif gift.CONSTRUCTOR_ID == 0x2cc73c8:  # StarGift
    #         print("Количество звезд:", gift.stars)
    #         print("Конвертация в звезды:", gift.convert_stars)


    filtered_gifts = []
    filtered_gifts_unique = []

    # Process each gift
    for user_gift in response.gifts:
        gift = user_gift.gift
        received_date = int(user_gift.date.timestamp())  # Convert datetime to Unix timestamp
        if gift.CONSTRUCTOR_ID == 0x2cc73c8:  # StarGift
            sender_id = user_gift.from_id.user_id if user_gift.from_id is not None else None
            gift_data = {
                "type": "StarGift",
                "id": gift.id,
                "stars": gift.stars,
                "convert_stars": gift.convert_stars,
                "sender_id": sender_id,
                "received_date": received_date
            }
            filtered_gifts.append(gift_data)
        elif gift.CONSTRUCTOR_ID == 0x5c62d151:  # StarGiftUnique
            collection_slug = gift.title.lower().replace(' ', '')
            # floor_price = floor_price_dict.get(collection_slug)
            gift_data = {
                "type": "StarGiftUnique",
                "id": gift.id,
                "title": gift.title,
                "slug": gift.slug,
                "num": gift.num,
                # "collection_floor_price_in_ton": floor_price,
                "availability_issued": gift.availability_issued,
                "availability_total": gift.availability_total,
                "received_date": received_date
            }
            filtered_gifts_unique.append(gift_data)
        else:
            continue

    return {
        "gifts": filtered_gifts,
        "gifts_unique": filtered_gifts_unique,
    }

async def get_more_info_unique_gift(client: TelegramClient, unique_gifts: list): 
    result = []
    for unique_gift in unique_gifts:
        if unique_gift.type == 'StarGiftUnique':
            request = await client(functions.payments.GetUniqueStarGiftRequest(
                slug=unique_gift.slug
            ))
            model = None
            for attr in request.gift.attributes:
                if hasattr(attr, 'name'):
                    model = attr.name
                    break
            gift_with_model = unique_gift.dict()
            if model:
                gift_with_model["model"] = model
            result.append(gift_with_model)

    return result