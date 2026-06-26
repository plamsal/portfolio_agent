import os
import requests


def notify_ntfy(message: str) -> None:
    topic = os.getenv("NTFY_TOPIC")
    print(f"[ntfy] topic exists: {bool(topic)}")
    if not topic:
        print("[ntfy] Missing NTFY_TOPIC — skipping")
        return
    try:
        response = requests.post(
            f"https://ntfy.sh/{topic}",
            data=message.encode("utf-8"),
            headers={"Title": "Portfolio Contact"},
            timeout=10,
        )
        print(f"[ntfy] Status: {response.status_code} | Response: {response.text}")
    except Exception as e:
        print(f"[ntfy] Error: {e}")


def notify_phone(message: str) -> None:
    notify_ntfy(message)


def notify_email(subject: str, body: str) -> None:
    notify_ntfy(f"{subject}\n\n{body}")
