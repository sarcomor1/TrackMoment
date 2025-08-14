FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
COPY wheelhouse/ ./wheelhouse/
RUN pip install --no-cache-dir --no-index --find-links=wheelhouse -r requirements.txt
COPY . .
RUN chmod +x wait-for-it.sh
RUN chmod +x entrypoint_migrate.sh
ENTRYPOINT ["./entrypoint_migrate.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
