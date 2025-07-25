# Dockerfile
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY backend/requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt
