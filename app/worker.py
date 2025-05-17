import asyncio
import aio_pika
import json
from app.notifications import send_email, send_sms, send_inapp

async def main():
    connection = await aio_pika.connect_robust("amqp://guest:guest@localhost/")
    channel = await connection.channel()
    queue = await channel.declare_queue("notifications", durable=True)

    async def handle(message: aio_pika.IncomingMessage):
        async with message.process():
            data = json.loads(message.body.decode())
            notif_type = data["type"]
            if notif_type == "email":
                send_email(data["user_id"], data["message"])
            elif notif_type == "sms":
                send_sms(data["user_id"], data["message"])
            elif notif_type == "inapp":
                send_inapp(data["user_id"], data["message"])

    await queue.consume(handle)
    print("🔁 Worker is running...")
    await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())