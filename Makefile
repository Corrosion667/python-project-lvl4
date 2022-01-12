MANAGE := poetry run python manage.py

install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=task_manager --cov-report xml

check: lint test

lint:
	poetry run flake8

migrate:
	$(MANAGE) migrate

shell:
	$(MANAGE) shell_plus

run:
	$(MANAGE) runserver