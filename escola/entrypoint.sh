pipenv run ./manage.py migrate &&
pipenv run ./manage.py collectstatic --noinput &&

if [ ${MULTISTAGE} -eq "PROD" ]
then
    pipenv run gunicorn -b 0.0.0.0:80 -w ${GUNICORN_WORKERS} -p /tmp/gunicorn_escola.pid escola.wsgi:application
else
    pipenv run gunicorn -D -b 0.0.0.0:80 -w ${GUNICORN_WORKERS} -p /tmp/gunicorn_escola.pid escola.wsgi:application && 
    pipenv run ./manage.py runserver 0.0.0.0:8000
fi
