FROM python:3.9.16-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . /app

ENV PYTHONPATH /app

CMD ["python3", "app/main.py"]