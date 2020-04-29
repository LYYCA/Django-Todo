FROM python:3

WORKDIR /code/backend

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY requirements.txt /code/backend
RUN pip install -r requirements.txt
COPY . /code/backend
