# uvicorn core.project.asgi:application --host 0.0.0.0 --port 8000 --reload
gunicorn core.project.wsgi:application --workers=4 --threads=4 --bind 0.0.0.0:8000 --reload