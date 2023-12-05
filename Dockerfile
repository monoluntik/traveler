FROM python:3.8

# Установка зависимостей
RUN apt-get update && apt-get install -y nginx
RUN pip install gunicorn

# Копирование кода проекта
COPY . /app
WORKDIR /app

# Установка зависимостей Python
RUN pip install -r requirements.txt

# Копирование конфигураций Nginx
COPY nginx.conf /etc/nginx/sites-available/default

# Экспозиция порта Gunicorn
EXPOSE 8000

# Запуск Gunicorn приложения
CMD ["gunicorn", "your_project.wsgi:application", "--bind", "0.0.0.0:8000"]
