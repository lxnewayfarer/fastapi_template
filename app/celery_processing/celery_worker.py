"""
Provides Celery back processing worker
"""


from celery import Celery
from celery.utils.log import get_task_logger

# Initialize Celery with RabbitMQ broker
celery_app = Celery(
    "celery_worker",
    broker='pyamqp://guest@localhost//'
)

celery_logger = get_task_logger(__name__)


@celery_app.task(acks_late=True)
# Runs cycle n times (10^8 ~ 5 sec)
def test_task(id_times: int):
    celery_logger.info("Test task started")

    counter = 0
    for i in range(id_times):
        counter += 1
    return counter
