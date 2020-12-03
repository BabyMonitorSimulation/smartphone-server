FROM python:3-alpine
RUN apk add --virtual .build-dependencies \ 
            --no-cache \
            python3-dev \
            build-base \
            linux-headers \
            pcre-dev

RUN apk add --no-cache pcre
WORKDIR /smartphone
COPY . /smartphone
RUN pip install -r /smartphone/requirements.txt
RUN pip install uwsgi
RUN apk del .build-dependencies && rm -rf /var/cache/apk/*
EXPOSE 5001
CMD ["uwsgi", "--ini", "/smartphone/wsgi.ini"]