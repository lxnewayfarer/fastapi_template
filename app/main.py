from fastapi import FastAPI, BackgroundTasks

from worker.celery_worker import test_celery

app = FastAPI()


def celery_on_message(body):
    print(body)

def background_on_message(task):
    print(task.get(on_message=celery_on_message, propagate=False))

@app.get("/")
async def root():
    return {"message": "Hello"}

@app.get("/{word}")
async def word(word: str):
    task = test_celery.delay(word)

    return {"message": "Word received"}
