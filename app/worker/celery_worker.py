from time import sleep
from celery import Celery, current_task
from celery.utils.log import get_task_logger

# Initialize celery
celery_app = Celery(
    "tasks",
    backend="redis://:password123@localhost:6379/0",
    broker="amqp://user:bitnami@localhost:5672//"
)

# Create logger - enable to display messages on task logger
celery_log = get_task_logger(__name__)

@celery_app.task
def test_celery(word: str) -> str:
    for i in range(1, 11):
        sleep(2)
        current_task.update_state(state='PROGRESS',
                                  meta={'process_percent': i*10})
    return f"test task return {word}"
