import requests

from .models import DeviceToken


EXPO_PUSH_URL = "https://exp.host/--/api/v2/push/send"


def send_push_notification(title, body, data=None):
    print("========== PUSH FUNCTION CALLED ==========")
    """
    Send a push notification to all registered devices.
    """

    device_tokens = DeviceToken.objects.values_list("token", flat=True)

    messages = []

    for token in device_tokens:
        messages.append({
    "to": token,
    "title": title,
    "body": body,
    "sound": "default",
    "data": data or {},
})

    if not messages:
        return

    response = requests.post(
        EXPO_PUSH_URL,
        json=messages,
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
    )

    print("Expo Response:", response.status_code)
    print(response.json())