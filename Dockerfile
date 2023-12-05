FROM python:3.8

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

CMD ["gunicorn", "core.wsgi:application", "-w", "4", "-b", "0.0.0.0:8000"]
