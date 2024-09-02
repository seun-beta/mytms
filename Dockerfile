# build stage
FROM python:3.10-slim-bullseye AS build

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends gcc

COPY requirements requirements

RUN pip wheel --no-cache-dir --no-deps --wheel-dir wheels -r requirements/base.txt


# final stage
FROM python:3.10-slim-bullseye

WORKDIR /app

COPY --from=build /app/wheels wheels
COPY --from=build /app/requirements/base.txt .

RUN pip install --no-cache wheels/*

ENV PYTHONPATH=/app