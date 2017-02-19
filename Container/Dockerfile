FROM debian:stable
MAINTAINER 0000000000zw <zareenmwilhelm@gmail.com>

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y python-pip python-dev build-essential

RUN pip install Flask

COPY . /flaskapp
ENV HOME=/flaskapp
WORKDIR /flaskapp

EXPOSE 8888

ENTRYPOINT ["python"]

CMD ["/flaskapp/flaskHello.py"]

HEALTHCHECK --interval=5s --timeout=3s --retries=3 \
 CMD curl -f http://localhost:80


