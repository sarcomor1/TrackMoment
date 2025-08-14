#!/bin/sh
set -e

./wait-for-it.sh db:5432 --timeout=30 --strict

python manage.py makemigrations
python manage.py migrate

echo "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
User.objects.filter(username='sarcomor').exists() or \
User.objects.create_superuser('sarcomor', 'sarcomor@gmail.com', '1231so2so')" \
| python manage.py shell

exec "$@"
