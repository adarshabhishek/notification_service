from pydantic import BaseModel
from typing import List

class Notification(BaseModel):
    user_id: int
    message: str
    type: str  # "email", "sms", "inapp"

class NotificationResponse(BaseModel):
    user_id: int
    notifications: List[Notification]