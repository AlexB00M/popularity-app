import asyncio
import aiohttp
import sys
import time

# Установка совместимой event loop политики на Windows
if sys.platform.startswith('win') and sys.version_info >= (3, 8):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

URL = 'http://127.0.0.1:8000/get_more_info_unique_gifts'  # замените на нужный путь

payload = [
        {
            "type": "StarGiftUnique",
            "id": 5852743271310164823,
            "title": "Desk Calendar",
            "slug": "DeskCalendar-87499",
            "num": 87499,
            "availability_issued": 319647,
            "availability_total": 374077,
            "received_date": 1744978988,
            "average_price": "Not found"
        },
        {
            "type": "StarGiftUnique",
            "id": 5841369102693696852,
            "title": "Jelly Bunny",
            "slug": "JellyBunny-39680",
            "num": 39680,
            "availability_issued": 68469,
            "availability_total": 129350,
            "received_date": 1744737238,
            "average_price": "Not found"
        },
        {
            "type": "StarGiftUnique",
            "id": 6023628865987937061,
            "title": "Record Player",
            "slug": "RecordPlayer-17826",
            "num": 17826,
            "availability_issued": 21073,
            "availability_total": 46888,
            "received_date": 1744127154,
            "average_price": "Not found"
        },
        {
            "type": "StarGiftUnique",
            "id": 5870954117328798459,
            "title": "Toy Bear",
            "slug": "ToyBear-1018",
            "num": 1018,
            "availability_issued": 52358,
            "availability_total": 57724,
            "received_date": 1746299416,
            "average_price": "Not found"
        },
        {
            "type": "StarGiftUnique",
            "id": 5846124821196309738,
            "title": "Snake Box",
            "slug": "SnakeBox-980",
            "num": 980,
            "availability_issued": 35185,
            "availability_total": 273898,
            "received_date": 1735651851,
            "average_price": "Not found"
        },
        {
            "type": "StarGiftUnique",
            "id": 5976367745942423026,
            "title": "Diamond Ring",
            "slug": "DiamondRing-28879",
            "num": 28879,
            "availability_issued": 31005,
            "availability_total": 32924,
            "received_date": 1744126798,
            "average_price": "Not found"
        },
        {
            "type": "StarGiftUnique",
            "id": 5972000786404607046,
            "title": "Desk Calendar",
            "slug": "DeskCalendar-276915",
            "num": 276915,
            "availability_issued": 319647,
            "availability_total": 374077,
            "received_date": 1745341544,
            "average_price": "Not found"
        }
]

async def send_post(session: aiohttp.ClientSession, idx: int):
    async with session.post(URL, json=payload) as response:
        text = await response.text()
        print(f"[{idx}] Status: {response.status}")
        return response.status, text

async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [send_post(session, i) for i in range(40)]
        results = await asyncio.gather(*tasks)
        return results

if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(f"Elapsed time: {end - start:.3f} seconds")