from fastapi import APIRouter, BackgroundTasks

from app.services.notification_service import write_notification

router = APIRouter(
    prefix="/background",
    tags=["Background Tasks"]
)



@router.post("/{email}")
async def send_notification(
    email: str,
    background_tasks: BackgroundTasks
):

    background_tasks.add_task(
        write_notification,
        email,
        message="some notification"
    )


    return {
        "message": "Notification sent in the background"
    }