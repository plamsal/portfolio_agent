import os
import requests


def notify_email(subject: str, body: str) -> None:
    api_key = os.getenv("RESEND_API_KEY")
    print(f"[Resend] api_key exists: {bool(api_key)}")
    if not api_key:
        print("[Resend] Missing RESEND_API_KEY — skipping")
        return
    try:
        response = requests.post(
            "https://api.resend.com/emails",
            headers={
                "Authorization": f"Bearer {api_key}",
                "Content-Type": "application/json",
            },
            json={
                "from": "Portfolio Agent <onboarding@resend.dev>",
                "to": ["lamsalservicenow@gmail.com"],
                "subject": subject,
                "text": body,
            },
            timeout=10,
        )
        print(f"[Resend] Status: {response.status_code} | Response: {response.text}")
    except Exception as e:
        print(f"[Resend] Error: {e}")


def notify_phone(message: str) -> None:
    notify_email(subject="Portfolio Contact", body=message)
