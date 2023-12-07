# Используем официальный образ Python
FROM python:3.8

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Создаем и устанавливаем рабочую директорию
WORKDIR /app

RUN apt-get install -y wait-for-it
# Копируем файл зависимостей
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копируем файлы проекта в контейнер
COPY . /app/
COPY proxy_params /etc/nginx/
COPY nginx.conf /etc/nginx/
# Открываем порт, на котором будет работать приложение
EXPOSE 8000

RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

# Команда для запуска приложения
CMD ["gunicorn", "core.wsgi:application", "-b", "0.0.0.0:8000"]
