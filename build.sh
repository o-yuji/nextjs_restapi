#!/usr/bin/env bash
# exit on error
set -o errexit
 
pip install -r requirements.txt
 
python manage.py collectstatic --noinput
python manage.py migrate
# python manage.py createsuperuser --username adminstrator --email admin@gmail.com --noinput