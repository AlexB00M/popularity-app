import requests
import time 

start = time.perf_counter()
response = requests.get('http://localhost:8000/api/users/user_gifts/')
end = time.perf_counter()
print(f"Время выполнения: {end - start:.4f} секунд")

# a = {"123": "999"}
# for i in a:
#     print(a[i])