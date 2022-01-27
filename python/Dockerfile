FROM python:3.8-alpine3.15
RUN apk update \
    && apk add linux-headers \
    && apk add build-base \
    && apk add bash 

ENV ENV_WORKDIR=/root/python-prometheus-client
WORKDIR ${ENV_WORKDIR}

