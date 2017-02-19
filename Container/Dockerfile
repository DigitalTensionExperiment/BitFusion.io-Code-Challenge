FROM debian:stable
MAINTAINER 0000000000zw <zareenmwilhelm@gmail.com>

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y python-pip python-dev build-essential curl

#RUN yum update -y
#RUN yum upgrade -y
#RUN yum install -y python-pip python-dev build-essential

RUN pip install Flask

COPY . /flaskapp
ENV HOME=/flaskapp
WORKDIR /flaskapp

EXPOSE 8888

ENV FLASK_APP=/flaskapp/flaskHello.py
#ENTRYPOINT ["python"]
# $ python -m flask run
CMD flask run --host=0.0.0.0 --port=8888

#CMD ["/bin/bash"]

HEALTHCHECK --interval=5s --timeout=3s --retries=3 \
 CMD curl -f http://localhost:8888


