# Используйте базовый образ с Python
FROM python:3.8

# Установите зависимости
COPY requirements.txt /app/
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

# Копируйте приложение в образ
COPY . /app/

# Определите переменные окружения, если необходимо

# Запустите приложение
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "core.wsgi:application"]
