from fastapi import APIRouter
from app.models import Notification, NotificationResponse
from app.utils import store_notification, get_user_notifications
import aio_pika
import json

router = APIRouter()
RABBITMQ_URL = "amqp://guest:guest@localhost/"

@router.post("/notifications")
async def send_notification(notification: Notification):
    store_notification(notification.user_id, notification.dict())

    connection = await aio_pika.connect_robust(RABBITMQ_URL)
    async with connection:
        channel = await connection.channel()
        queue = await channel.declare_queue("notifications", durable=True)
        await channel.default_exchange.publish(
            aio_pika.Message(body=json.dumps(notification.dict()).encode()),
            routing_key=queue.name
        )
    return {"message": "Notification queued"}

@router.get("/users/{user_id}/notifications", response_model=NotificationResponse)
def get_notifications(user_id: int):
    return NotificationResponse(
        user_id=user_id,
        notifications=get_user_notifications(user_id)
    )