import asyncio
import aiohttp
import sys
import time

# Установка совместимой event loop политики на Windows
if sys.platform.startswith('win') and sys.version_info >= (3, 8):
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

URL = 'http://127.0.0.1:8000/api/users/user_gifts/'  # замените на нужный путь

async def send_post(session: aiohttp.ClientSession, idx: int):
    async with session.get(URL) as response:
        text = await response.text()

    
    print(f"[{idx}] Status: {response.status}")

    
    return response.status, text

async def main():
    async with aiohttp.ClientSession() as session:
        results = []
        for i in range(20):
            start = time.perf_counter()
            result = await send_post(session, i)
            results.append(result)
            end = time.perf_counter()
            print(f"Request time: {end - start:.3f} seconds")
            await asyncio.sleep(0.01)  # пауза 0.5 секунды между запросами
        return results


if __name__ == '__main__':
    start = time.perf_counter()
    asyncio.run(main())
    end = time.perf_counter()
    print(f"Elapsed time: {end - start:.3f} seconds")