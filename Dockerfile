FROM python:3.7-alpine
MAINTAINER Pooria Skremed


COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /pgu
WORKDIR /pgu
COPY ./pgu /pgu

# update apk repo
RUN echo "http://dl-4.alpinelinux.org/alpine/v3.8/main" >> /etc/apk/repositories && \
    echo "http://dl-4.alpinelinux.org/alpine/v3.8/community" >> /etc/apk/repositories

# install chromedriver
RUN apk update
RUN apk add chromium chromium-chromedriver

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser -D user
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
COPY ./pgu/vol /vol
USER user
