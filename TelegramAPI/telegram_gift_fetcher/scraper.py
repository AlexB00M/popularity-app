from typing import Optional
from bs4 import BeautifulSoup
import urllib.parse
import aiohttp
import asyncio

async def get_unique_gift_price(session: aiohttp.ClientSession, url: str) -> float:
    async with session.get(url) as response:
        response_text = await response.text()
        soup = BeautifulSoup(response_text, 'lxml')
        try:
            price = soup.find('div', class_='tm-grid-item-value tm-value icon-before icon-ton').get_text(strip=True)
            return float(price)
        except Exception as e:
            print(e)
            return 'Average price not found'

def build_fragment_url(title: str, model: str, sort: str) -> str: # sort= price_asc/price_desc
    base_url = "https://fragment.com/gifts"
    slug = title.lower().replace(' ', '')
    params = {
        'attr[Model]': f'["{model}"]'
    }
    query_string = urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    return f"{base_url}/{slug}?sort={sort}&filter=sold&{query_string}"

# print(build_fragment_url('Snake Box', 'Emerald', 'price_asc'))

async def get_unique_gift_average_price(unique_gift_data: dict) -> Optional[float]:
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                          "(KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

        title = unique_gift_data['title']
        model = unique_gift_data['model']
        url_asc = build_fragment_url(title, model, 'price_asc')
        url_desc = build_fragment_url(title, model, 'price_desc')

        async with aiohttp.ClientSession() as session:
            # Запускаем оба запроса параллельно
            min_price_poc = get_unique_gift_price(session, url_asc)
            max_price_poc  = get_unique_gift_price(session, url_desc)

            min_price, max_price = await asyncio.gather(min_price_poc, max_price_poc)
            if min_price != 'Average price not found' or max_price != 'Average price not found':
                average_price = (max_price + min_price)/2
                print(f'{unique_gift_data['title']} | {unique_gift_data['model']} | Max_price - {max_price} | Min_price = {min_price} | Average - {average_price}')

                return average_price
            else:
                return 'Average price not found'
    except Exception as e:
        print(f'Error getting gift collection floor price: {e}')
        return None