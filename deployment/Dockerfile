FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    curl \
    build-essential

ENV POETRY_HOME=/opt/poetry
ENV PATH="/opt/poetry/bin:$PATH"

RUN curl -sSL https://install.python-poetry.org | python3 - \
    && poetry --version

WORKDIR /app

COPY pyproject.toml poetry.lock* ./
COPY README.md ./

RUN python3 -m pip install poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

COPY . .

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "food_helper.main:app", "--host", "0.0.0.0", "--port", "8000", "--factory"]
