from fastapi import APIRouter, BackgroundTasks

router = APIRouter(
    prefix="/background",
    tags=["Background Tasks"]
)


def write_notification(
    email: str,
    message: str = ""
):

    with open(
        "log.txt",
        mode="a"
    ) as file:
        content = (
            f"notification for {email}: {message}\n"
        )
        file.write(content)



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