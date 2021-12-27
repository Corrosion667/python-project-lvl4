install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=task_manager --cov-report xml

check: lint test

build: check
	poetry build

lint:
	poetry run flake8