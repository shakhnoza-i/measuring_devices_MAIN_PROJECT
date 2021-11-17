FROM ubuntu:20.04

ENV PYTHONUNBUFFERED 1 

ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV TZ=Asia/Almaty
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN apt-get update
RUN apt-get -yq upgrade
RUN apt-get update
RUN apt-get -yq install libsnappy-dev graphviz graphviz-dev pkg-config
RUN apt-get install -yq build-essential libssl-dev libffi-dev python3-dev
RUN apt-get install -yq python3-setuptools
RUN apt-get install -yq python3-pip
RUN apt-get install -yq git mc postgresql-client 
RUN apt-get install -yq libxml2-dev libxslt1-dev 
RUN apt-get install -yq gdal-bin
RUN apt-get install -yq libgdal-dev


COPY ./requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt 

RUN mkdir /meter_project

WORKDIR /meter_project

COPY ./meter_project /meter_project


RUN adduser --no-create-home user
# switch docker to this user
USER user

# RUN chown nobody:nogroup "celerybeat-schedule"
# USER nobody
# CMD ["celery", "-A", "meter_project.celery_app", "-E", "-B"]
