#!/bin/sh

python manage.py collectstatic

gunicorn news.wsgi:application --bind 0.0.0.0:$PORT --capture-output