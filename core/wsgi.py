import os
import sys
import logging
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
application = get_wsgi_application()

# Добавьте следующие строки для настройки логирования
logger = logging.getLogger('gunicorn.error')
application = logging.handlers.WatchedFileHandler('/app/logs/gunicorn.log')
logger.addHandler(application)
