import hashlib
import hmac
import time
from urllib.parse import parse_qs

def validate_init_data(init_data: str, bot_token: str, max_age: int = 86400):
    parsed = dict([part.split('=') for part in init_data.split('&') if '=' in part])
    hash_from_telegram = parsed.pop('hash', None)
    auth_date = int(parsed.get('auth_date', 0))
    if time.time() - auth_date > max_age:
        return False

    data_check_string = "\n".join(f"{k}={v}" for k, v in sorted(parsed.items()))
    secret_key = hashlib.sha256(bot_token.encode()).digest()
    calculated_hash = hmac.new(secret_key, data_check_string.encode(), hashlib.sha256).hexdigest()

    return hmac.compare_digest(calculated_hash, hash_from_telegram)