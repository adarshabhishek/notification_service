user_notifications = {}

def store_notification(user_id: int, notification: dict):
    if user_id not in user_notifications:
        user_notifications[user_id] = []
    user_notifications[user_id].append(notification)

def get_user_notifications(user_id: int):
    return user_notifications.get(user_id, [])