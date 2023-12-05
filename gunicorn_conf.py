workers = 4  # Adjust the number of workers based on your system's capabilities
worker_class = 'sync'  # You can use 'sync', 'gevent', or 'eventlet' based on your needs

bind = '0.0.0.0:8000'  # Binding address and port for Gunicorn
timeout = 60  # Adjust the timeout as needed

# Logging configuration
accesslog = '-'  # Use '-' to log to stdout
errorlog = '-'   # Use '-' to log to stderr
loglevel = 'info'  # Adjust the log level based on your needs
