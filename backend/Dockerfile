FROM python:3.12.1-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# RUN apk update -y && \
#     apk install -y python3-dev \
#     gcc \
#     musl-dev \
#     libpq-dev \
#     nmap

RUN pip install --upgrade pip

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh