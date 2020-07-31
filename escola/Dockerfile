FROM basiliocode/python3-alpine3

RUN apk add openrc --no-cache

RUN apk add nginx
RUN rc-update add nginx

WORKDIR /app/escola

COPY . /app/escola
RUN mkdir /app/media

RUN pipenv install

RUN pipenv run ./manage.py check

EXPOSE 80
