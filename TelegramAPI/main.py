from fastapi import FastAPI, Request, HTTPException
from telethon import TelegramClient
from telegram_gift_fetcher import get_user_gifts, get_more_info_unique_gift, get_unique_gift_average_price, get_lottie_animation_json
from contextlib import asynccontextmanager
import environ
from pydantic import BaseModel
from typing import List, Optional, Union
import asyncio
from telethon import functions
from telethon.tl.types import Document, StarGiftAttributeModel
import os

env = environ.Env()
environ.Env.read_env('.env')

api_id = env('API_ID')
api_hash = env('API_HASH')

API_TELEGRAM_SECRET_TOKEN = env('API_TELEGRAM_SECRET_TOKEN')

client = TelegramClient('session', api_id, api_hash)

@asynccontextmanager
async def lifespan(app: FastAPI):
    await client.start()
    print("Telegram client started")
    yield
    await client.disconnect()
    print("Telegram client disconnected")

app = FastAPI(lifespan=lifespan)

@app.middleware("http")
async def verify_token(request: Request, call_next):

    auth_header = request.headers.get("Authorization")
    expected = f"Bearer {API_TELEGRAM_SECRET_TOKEN}"

    if auth_header != expected:
        raise HTTPException(status_code=403, detail="Unauthorized")

    return await call_next(request)

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
    average_price: Optional[Union[str, int]] = None

@app.post("/get_more_info_unique_gifts")
async def get_more_info_unique_gifts(unique_gifts: List[UniqueGift]):
    unique_gifts_data = await get_more_info_unique_gift(client, unique_gifts) 

    return unique_gifts_data


@app.get("/get_telegram_gifts")
async def get_telegram_gifts():
    result = await client(functions.payments.GetStarGiftsRequest(hash=0))
    response = []

    async def process_gift(gift):
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

        return template
    
    tasks = [process_gift(gift) for gift in result.gifts]

    response = await asyncio.gather(*tasks)

    return response

import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=9000, reload=True)