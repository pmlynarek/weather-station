FROM python:3.8-slim


ENV PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1 PIP_DISABLE_PIP_VERSION_CHECK=1

COPY requirements.txt /requirements.txt
COPY requirements-dev.txt /requirements-dev.txt
RUN pip install -r requirements-dev.txt

WORKDIR /sanic
COPY . .

ENV SANIC_SERVER_PORT 8000
ENV SANIC_SERVER_HOST 0.0.0.0

EXPOSE 8000
