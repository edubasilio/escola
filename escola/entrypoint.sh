#!/bin/bash

### WAITING POSTGRES START ###
RETRIES=7
while [ "$RETRIES" -gt 0 ]
do
  echo "Waiting for postgres server, $RETRIES remaining attempts..."
  RETRIES=$((RETRIES-1))
  PG_STATUS="$(pg_isready -h ${DB_HOST} -p 5432 -d ${DB_NAME} -U ${DB_USER})"
  PG_EXIT=$(echo $?)
  echo "Postgres Status: $PG_EXIT - $PG_STATUS"
  if [ "$PG_EXIT" = "0" ]; then
      RETRIES=0
  else
      sleep 5
  fi
done

### DJANGO MIGRATE AND COLLECT STATIC FILES ###
pipenv run ./manage.py migrate &&
pipenv run ./manage.py collectstatic --noinput &&

### START WEBSERVER ###
if [ ${MULTISTAGE} = "PROD" ]; then
    pipenv run gunicorn -b 0.0.0.0:80 -w ${GUNICORN_WORKERS} -p /tmp/gunicorn_escola.pid escola.wsgi:application
else
    pipenv run gunicorn -D -b 0.0.0.0:80 -w 2 -p /tmp/gunicorn_escola.pid escola.wsgi:application && 
    pipenv run ./manage.py runserver 0:8000
fi
