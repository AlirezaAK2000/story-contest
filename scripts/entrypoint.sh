#!/bin/sh

set -e

python manage.py collectstatic --noinput

gunicorn --env DJANGO_SETTINGS_MODULE=first.settings first.wsgi:application --bind 0.0.0.0:8000