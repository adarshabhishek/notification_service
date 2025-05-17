def send_email(user_id: int, message: str):
    print(f"📧 Email sent to user {user_id}: {message}")

def send_sms(user_id: int, message: str):
    print(f"📱 SMS sent to user {user_id}: {message}")

def send_inapp(user_id: int, message: str):
    print(f"🔔 In-app notification for user {user_id}: {message}")