# TRACKMOMENT
type (docker compose up --build) in the project directory
docker exec -it my_container_name /bin/bash
python manage.py makemigrations
python manage.py migrate
docker stop your_web_container_name
docker stop your_db_container_name
docker-compose up
Open http://localhost:8001/ in the Brother

برای ورود به دیتابیس
docker exec -it your_db_container_name psql -U test -d test

ایجاد یوزر
python manage.py createsuperuser
