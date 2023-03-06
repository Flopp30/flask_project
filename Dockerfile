FROM python:3.9.1-buster

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt && pip install psycopg2-binary==2.9.5
COPY app/wsgi.py wsgi.py
COPY app/blog ./blog
