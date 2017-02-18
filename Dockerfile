FROM debian:stable
MAINTAINER 0000000000zw <zareenmwilhelm@gmail.com>

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y python-pip python-dev build-essential

RUN pip install Flask

RUN mkdir flask
COPY flaskHello.py flask/flaskHello.py
#RUN python flask/flaskHello.py

ENV FLASK_APP=flask/flaskHello.py

EXPOSE 8888
