from fastapi import FastAPI, HTTPException
from telethon import TelegramClient
from telegram_gift_fetcher import get_user_gifts, get_more_info_unique_gift, get_unique_gift_average_price
from contextlib import asynccontextmanager
import environ
from pydantic import BaseModel
from typing import List
import asyncio
from telethon import functions
import zipfile
from telethon.tl.types import Document, StarGiftAttributeModel
import json 
import io
import lottie
import os
import tempfile

env = environ.Env()
environ.Env.read_env('.env')

api_id = env('API_ID')
api_hash = env('API_HASH')

client = TelegramClient('session', api_id, api_hash)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await client.start()
    print("Telegram client started")
    yield
    await client.disconnect()
    print("Telegram client disconnected")

app = FastAPI(lifespan=lifespan)

@app.get("/user_gifts/{username}")
async def user_gifts(username: str):
    try:
        response = {
            "gifts": [],
            "gifts_unique": [],
        }
        offset = 0
        while True:
            gifts = await get_user_gifts(client, username, offset=f'{offset}', limit=100)
            if isinstance(gifts, str):
                break
            if len(gifts["gifts"]) == 0 and len(gifts["gifts_unique"]) == 0:
                break

            response["gifts"].extend(gifts["gifts"])
            response["gifts_unique"].extend(gifts["gifts_unique"])

            if (len(gifts["gifts"]) + len(gifts["gifts_unique"])) <= 100:
                break
            offset += 100

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return response


class UniqueGift(BaseModel):
    type: str
    id: int
    title: str
    slug: str
    num: int
    availability_issued: int
    availability_total: int
    received_date: int

async def get_lottie_animation_json(client, doc):
    with tempfile.NamedTemporaryFile(suffix=".tgs", delete=False) as tmp_file:
        temp_filename = tmp_file.name

    try:
        await client.download_media(doc, file=temp_filename)
        print(f"Стикер временно сохранён как: {temp_filename}")

        lottie_animation_json = lottie.parsers.tgs.parse_tgs_json(temp_filename, encoding="utf-8")

    finally:
        if os.path.exists(temp_filename):
            os.remove(temp_filename)
            print(f"Временный файл {temp_filename} удалён")

    return lottie_animation_json

async def get_lottie_json_for_gift(gift):
    result = await client(functions.payments.GetUniqueStarGiftRequest(
        slug='RecordPlayer-17826'
    ))
    doc = None
    for attr in result.gift.attributes:
        if isinstance(attr, StarGiftAttributeModel):
            doc = attr.document
    if doc: 
        if isinstance(doc, Document):
            lottie_animation_json = await get_lottie_animation_json(client, doc)
            return lottie_animation_json

async def update_unique_gifts(unique_gifts_data, batch_size):
    for i in range(0, len(unique_gifts_data), batch_size):
        batch = unique_gifts_data[i:i + batch_size]

        price_tasks = [get_unique_gift_average_price(gift) for gift in batch]
        lottie_tasks = [get_lottie_json_for_gift(gift) for gift in batch]

        prices, lotties = await asyncio.gather(
            asyncio.gather(*price_tasks),
            asyncio.gather(*lottie_tasks),
        )

        for gift, avg_price, lottie_json in zip(batch, prices, lotties):
            gift["average_price"] = avg_price
            gift["lottie_animation_json"] = {} #lottie_json

    return unique_gifts_data

@app.post("/get_more_info_unique_gifts")
async def get_more_info_unique_gifts(unique_gifts: List[UniqueGift]):
    unique_gifts_data = await get_more_info_unique_gift(client, unique_gifts)
    result = await update_unique_gifts(unique_gifts_data, batch_size=5)

    return result

@app.get("/get_telegram_gifts")
async def get_telegram_gifts():
    response = []
    result = await client(functions.payments.GetStarGiftsRequest(hash=0))

    for gift in result.gifts:
        template = {
            "type": gift.__class__.__name__,
            "id": gift.id,
            "sold_out": gift.sold_out,
            "price": gift.stars,
            "convert_stars": gift.convert_stars,
        }

        doc = gift.sticker
        if isinstance(doc, Document):
            filename = f"telegram_animations/gifts/{gift.id}_AnimatedSticker.tgs"
            if not os.path.exists(filename):
                await client.download_media(doc, file=filename)	
                print(f"Стикер сохранён как: {filename}")

            lottie_animation_json = await get_lottie_animation_json(client, doc)
            template['lottie_animation_json'] = lottie_animation_json
        response.append(template)

    return response
