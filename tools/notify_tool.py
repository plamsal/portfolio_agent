import os
import smtplib
import requests
from email.mime.text import MIMEText
from agents import function_tool


@function_tool
def notify_phone(message: str) -> dict:
    """
    Send a push notification to Pratik's phone via Pushover.
    Use this when someone wants to get in touch or leaves their contact details.
    """
    response = requests.post(
        "https://api.pushover.net/1/messages.json",
        data={
            "token": os.getenv("PUSHOVER_TOKEN"),
            "user":  os.getenv("PUSHOVER_USER"),
            "message": message,
        }
    )
    return {"status": "sent", "code": response.status_code}


@function_tool
def notify_email(subject: str, body: str) -> dict:
    """
    Send an email notification to Pratik.
    Use this when someone wants to get in touch or leaves their contact details.
    """
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"]    = os.getenv("NOTIFY_EMAIL_FROM")
    msg["To"]      = os.getenv("NOTIFY_EMAIL_TO")

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(
            os.getenv("NOTIFY_EMAIL_FROM"),
            os.getenv("NOTIFY_EMAIL_PASSWORD")
        )
        server.send_message(msg)

    return {"status": "sent"}
