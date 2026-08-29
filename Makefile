.PHONY: install migrate seed run test docker-build docker-run clean

install:
	pip install -r requirements.txt

migrate:
	python manage.py makemigrations
	python manage.py migrate

seed:
	python -c "import os, django; os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'educlear_backend.settings'); django.setup(); from knowledge_base.seed_data import seed_database; seed_database()"

run:
	python main.py

test:
	pytest --cov=. tests/

docker-build:
	docker build -t educlear-platform:latest .

docker-run:
	docker run -p 8000:8000 educlear-platform:latest

clean:
	rm -rf __pycache__ *.pyc db.sqlite3 .coverage htmlcov
