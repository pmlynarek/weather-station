FROM python:3.7-slim
MAINTAINER Patryk Młynarek


# Start Installing the Basic Dependencies
RUN pip install --upgrade pip
RUN pip install gunicorn

RUN mkdir -p /sanic/config
RUN mkdir -p /sanic/weather

COPY config/* /sanic/config/
COPY weather/ /sanic/weather/
COPY requirements.txt /sanic
COPY run.py /sanic/run.py
COPY .env /sanic/.env

WORKDIR /sanic
RUN find . -type f

ENV SANIC_SERVER_PORT 8000
ENV SANIC_SERVER_HOST 0.0.0.0

EXPOSE 8000


ENTRYPOINT ["python", "run.py"]

