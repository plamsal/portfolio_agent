import os
import smtplib
import requests
from email.mime.text import MIMEText


def notify_phone(message: str) -> None:
    """Send a Pushover push notification. Silently fails if not configured."""
    token = os.getenv("PUSHOVER_TOKEN")
    user = os.getenv("PUSHOVER_USER")
    if not token or not user:
        return
    try:
        requests.post(
            "https://api.pushover.net/1/messages.json",
            data={"token": token, "user": user, "message": message},
            timeout=5,
        )
    except Exception:
        pass


def notify_email(subject: str, body: str) -> None:
    """Send a Gmail notification. Silently fails if not configured or credentials are wrong."""
    from_addr = os.getenv("NOTIFY_EMAIL_FROM")
    to_addr = os.getenv("NOTIFY_EMAIL_TO")
    password = os.getenv("NOTIFY_EMAIL_PASSWORD")
    if not from_addr or not to_addr or not password:
        return
    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = from_addr
        msg["To"] = to_addr
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, timeout=10) as server:
            server.login(from_addr, password)
            server.send_message(msg)
    except Exception:
        pass
