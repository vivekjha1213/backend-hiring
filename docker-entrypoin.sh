#!/bin/bash

# Wait for Redis to be ready
until redis-cli -h redis ping; do
  echo "Redis is unavailable - sleeping"
  sleep 1
done

echo "Redis is up - executing command"

# Apply database migrations
python manage.py migrate

# Start Celery worker in background
celery -A vanderval worker -Q high,medium,low -l info &

# Start Django server
python manage.py runserver 0.0.0.0:8000

# docker-compose.yml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    depends_on:
      - redis
    environment:
      - CELERY_BROKER_URL=redis://redis:6379/0
      - CELERY_RESULT_BACKEND=redis://redis:6379/0
      - DEBUG=1
      - DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1

  redis:
    image: redis:latest
    ports:
      - "6379:6379"

  celery:
    build: .
    command: celery -A vanderval worker -Q high,medium,low -l info
    volumes:
      - .:/app
    depends_on:
      - redis
    environment:
      - CELERY_BROKER_URL=redis://redis:6379/0
      - CELERY_RESULT_BACKEND=redis://redis:6379/0

#