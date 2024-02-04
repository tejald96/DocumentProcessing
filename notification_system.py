# notification_system.py

def send_notification(email, message):

    try:
        print(f"Notification sent to {email}: {message}")
        return True
    except Exception as e:
        print(f"Notification sending failed: {e}")
        return False
