#!/bin/sh
set -e

./wait-for-it.sh db:5432 --timeout=30 --strict

python manage.py makemigrations
python manage.py migrate

exec "$@"
