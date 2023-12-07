import os
from django.core.wsgi import get_wsgi_application
from gunicorn_logger import Logger  # добавьте эту строку

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
application = get_wsgi_application()
application = Logger(application)  # добавьте эту строку
