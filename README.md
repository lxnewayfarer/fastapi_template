# *FastAPI* template bundled in *pipenv* and including *Celery*


## Installation:
`pipenv install`

## Run:
- To start Rabbitmq, Redis, Celery-flower, run: `docker-compose up`
- Then to start main application, run: `pipenv run python main.py`

## Description of dependencies:
*You may check list of dependencies in Pipfile*
FastAPI framework - web framework for building APIs. Features: high perfomance, minimalistic, validation for most data types, automatic Swagger/Redoc documentation, async support
Uvicorn - ASGI server implementation, using uvloop and httptools
Celery - Distributed task queue
Pydantic - Data validation and settings management using Python type hinting
Redis - in-memory data structure store

Python 3.8

