# *FastAPI* template bundled in *pipenv* and including *Celery* back processing with RabbitMQ broker in docker-compose

This is an another yet FastAPI template which was bundled with pipenv, and using as simplified as possible 
docker-compose with clean official modules and containers to run RabbitMQ and Flower UI to check Celery workers. 
Including one route and one worker as example. And some linting.

Comprehensive documentation of FastAPI with common project structure and everything else: https://fastapi.tiangolo.com/tutorial/bigger-applications/

Documentation of Celery: https://docs.celeryproject.org/en/stable/getting-started/introduction.html

## Installation:
`pipenv install`


## Run:
- To start Rabbitmq and Celery-flower, run: `docker-compose up`
- Then to start Celery worker, **go to the /app directory** and run: `celery -A celery_processing.celery_worker worker --loglevel=INFO`
- And to start FastAPI application, run: `pipenv run uvicorn main:app --reload --port 8000`

Ports:
- Your API will be available on http://localhost:8000
- Flower: http://localhost:5555 (Basic auth login/password: test:test)
- Swagger UI: http://localhost:8000/docs
- RabbitMQ UI: http://localhost:15672 (Auth: guest:guest. You can update environment in docker-compose to set your credentials for user and admin)

## Short description of dependencies:
*You can check list of dependencies in Pipfile*

- FastAPI framework - web framework for building APIs. Features: high perfomance, minimalistic, validation for most data types, automatic Swagger/Redoc documentation, async support
- Uvicorn - ASGI server implementation, using uvloop and httptools
- Celery - Distributed task queue
- Pydantic - Data validation and settings management using Python type hinting

**Python 3.8** is necessary for *pipenv*

## Notes:
- If you changed your worker, you have to restart Celery to use updated worker
- If you getting Pylint warning "Import 'module_name' could not be resolved" , in VSCode you can edit the `setting.json` file. If you add `"python.analysis.useImportHeuristic": true`, the linting error will be removed. (Added to `.vscode/setting.json`)
