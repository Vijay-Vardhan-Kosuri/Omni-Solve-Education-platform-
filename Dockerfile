FROM python:3.13-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python -c "import os, django; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'educlear_backend.settings'); django.setup(); from knowledge_base.seed_data import seed_database; seed_database()"

EXPOSE 8000

CMD ["python", "main.py"]
