RETRIES=7

until psql -h ${DB_HOST} -U ${DB_USER} -d ${DB_NAME} -c "select 1" > /dev/null 2>&1 || [ $RETRIES -eq 0 ]; do
  echo "Waiting for postgres server, $((RETRIES--)) remaining attempts..."
  sleep 5
done

pipenv run ./manage.py migrate &&
pipenv run ./manage.py collectstatic --noinput &&

if [ ${MULTISTAGE} -eq "PROD" ]
then
    pipenv run gunicorn -b 0.0.0.0:80 -w ${GUNICORN_WORKERS} -p /tmp/gunicorn_escola.pid escola.wsgi:application
else
    pipenv run gunicorn -D -b 0.0.0.0:80 -w ${GUNICORN_WORKERS} -p /tmp/gunicorn_escola.pid escola.wsgi:application && 
    pipenv run ./manage.py runserver 0.0.0.0:8000
fi
