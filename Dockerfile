FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
COPY wheelhouse/ ./wheelhouse/
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN chmod +x wait-for-it.sh
RUN chmod +x entrypoint_migrate.sh
ENTRYPOINT ["./entrypoint_migrate.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
