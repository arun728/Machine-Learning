FROM python:3.7

ENV PYTHONUNBUFFERED 1

RUN mkdir /proxy

WORKDIR /proxy

ADD . /proxy

RUN pip install -r requirements.txt

