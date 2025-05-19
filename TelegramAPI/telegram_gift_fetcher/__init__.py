import asyncio
from telethon import functions
from typing import Optional, Dict
from telethon import TelegramClient
from telethon.tl.types import InputUser
from .tl_objects import GetUserStarGifts
from .scraper import get_unique_gift_average_price
import tempfile
import os 
import lottie
from telethon.tl.types import Document, MessageEntityCustomEmoji, StarGiftAttributeModel, StarGiftAttributePattern, StarGiftAttributeBackdrop, StarGiftAttributeOriginalDetails
import base64

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

async def get_lottie_animation_json(client, doc):
    with tempfile.NamedTemporaryFile(suffix=".tgs", delete=False) as tmp_file:
        temp_filename = tmp_file.name
    try:
        result = await client.download_media(doc, file=temp_filename)
        if doc.mime_type == "application/x-tgsticker":
            print(f"Стикер временно сохранён как: {temp_filename}")
            
            lottie_animation_json = lottie.parsers.tgs.parse_tgs_json(temp_filename, encoding="utf-8")
            return {"data": lottie_animation_json, "is_animated": True}
        elif doc.mime_type == "image/webp":
            with open(temp_filename, "rb") as f:
                image_bytes = f.read()
                image_base64 = base64.b64encode(image_bytes).decode("utf-8")

            return {"data": image_base64, "is_animated": False}
    finally:
        if os.path.exists(temp_filename):
            os.remove(temp_filename)
            print(f"Временный файл {temp_filename} удалён")


async def get_lottie_animations_emoji(client, entities):
    emojis_temp = [
        {
            "offset": entity.offset,
            "length": entity.length,
            "document_id": entity.document_id
        }
        for entity in entities
        if isinstance(entity, MessageEntityCustomEmoji)
    ]

    docs = await client(functions.messages.GetCustomEmojiDocumentsRequest(
        document_id=[e["document_id"] for e in emojis_temp]
    ))

    emojis = []
    for emoji_data, doc in zip(emojis_temp, docs):
        image_base64 = await get_lottie_animation_json(client, doc)
        emojis.append({
            "offset": emoji_data["offset"],
            "length": emoji_data["length"],
            "document_id": doc.id,
            "is_animated": image_base64["is_animated"],
            "image": image_base64["data"]
        })

    return emojis

async def process_unique_gift(client, unique_gift):
    request = await client(functions.payments.GetUniqueStarGiftRequest(slug=unique_gift.slug))

    gift_data = unique_gift.dict()

    doc = None

    model = None
    pattern = None
    backdrop = None

    sender_id = None
    message_text = None

    emojis = []
    # print(request.gift) # посмотреть message_id
    for attr in request.gift.attributes:
        if isinstance(attr, StarGiftAttributeModel):
            model = attr.name
            doc = attr.document  # если нужно сохранить document, можно сделать отдельно model_doc = attr.document
        elif isinstance(attr, StarGiftAttributePattern):
            pattern = attr.name
        elif isinstance(attr, StarGiftAttributeBackdrop):
            backdrop = attr.name
        elif isinstance(attr, StarGiftAttributeOriginalDetails):
            sender_id = attr.sender_id.user_id
            message_text = attr.message.text
            entities = attr.message.entities
            emojis = await get_lottie_animations_emoji(client, entities)


    if model:
        gift_data["model"] = model
    if pattern:
        gift_data["pattern"] = pattern
    if backdrop:
        gift_data["backdrop"] = backdrop
    if sender_id:
        gift_data['sender_id'] = sender_id
    if message_text:
        gift_data['message_text'] = message_text
        if emojis:
            gift_data['emojis'] = emojis

    tasks = []
    
    if doc and isinstance(doc, Document):
        tasks.append(get_lottie_animation_json(client, doc))

    if gift_data['average_price'] is None:
        tasks.append(get_unique_gift_average_price(gift_data))

    results = await asyncio.gather(*tasks)

    i = 0
    if doc and isinstance(doc, Document):
        gift_data['lottie_animation_json'] = results[i]["data"]
        i += 1

    if gift_data['average_price'] is None:
        gift_data['average_price'] = results[i]

    return gift_data

semaphore = asyncio.Semaphore(20)

async def process_unique_gift_limited(client, gift):
    async with semaphore:
        return await process_unique_gift(client, gift)

async def get_more_info_unique_gift(client, unique_gifts):
    tasks = [
        process_unique_gift_limited(client, gift)
        for gift in unique_gifts
        if gift.type == 'StarGiftUnique'
    ]
    results = await asyncio.gather(*tasks)
    return [res for res in results if res is not None]