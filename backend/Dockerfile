FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt /app

RUN apt-get update && apt-get -y install libpq-dev gcc && pip install psycopg2

RUN pip install -r /app/requirements.txt --no-cache-dir
RUN pip install gunicorn

COPY ./ /app

CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0.0.0.0:8000"]