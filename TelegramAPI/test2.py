from telethon.sync import TelegramClient
from telethon import functions, types
import environ

env = environ.Env()
environ.Env.read_env('.env')

api_id = env('API_ID')
api_hash = env('API_HASH')

with TelegramClient("session", api_id, api_hash) as client:
    result = client(functions.payments.GetSavedStarGiftsRequest(
        peer='5547201569',
        offset='some string here',
        limit=100,
        exclude_unsaved=True,
        exclude_saved=True,
        exclude_unlimited=True,
        exclude_limited=True,
        exclude_unique=True,
        sort_by_value=True
    ))

    print(result.stringify())