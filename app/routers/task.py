"""
Provides FastAPI /task route with GET method
"""

from typing import Optional
from fastapi import File, UploadFile, BackgroundTasks, APIRouter
from celery_processing.celery_worker import test_task

# Route with prefix "/task"
router = APIRouter(
    prefix="/task",
    tags=["task"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
# Just GET method. Others are the same
async def task_get(id: Optional[int] = None):
    # runs celery task with this ID (cycle N=id times)
    test_task.delay(id)

    return {
        "status": "ok",
        "data": {
            "id": id,
            "task": "task"
        }
    }
