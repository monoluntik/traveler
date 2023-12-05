# Используйте образ Python для вашего приложения
FROM python:3.8-slim

# Установите переменную окружения PYTHONUNBUFFERED
ENV PYTHONUNBUFFERED 1

# Создайте и установите директорию приложения
RUN mkdir /app
WORKDIR /app

# Установите зависимости
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Скопируйте код приложения в контейнер
COPY . /app/
