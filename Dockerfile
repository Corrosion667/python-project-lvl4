FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    POETRY_VERSION=1.2.0b1

RUN apt-get update \
    && apt-get -y install libpq-dev gcc

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR /task-manager

COPY poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --without dev

COPY . .

RUN poetry run python manage.py migrate

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]