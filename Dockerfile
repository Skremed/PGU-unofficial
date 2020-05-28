FROM python:3.7-alpine
MAINTAINER Pooria Skremed




COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /pgu
WORKDIR /pgu
COPY ./pgu /pgu

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user