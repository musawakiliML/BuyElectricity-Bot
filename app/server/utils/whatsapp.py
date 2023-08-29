from app.server.config.config import Settings
import requests

settings = Settings()

def send_whatsapp_message(phone_number, message):
    headers = {"Authorization": settings.WHATSAPP_TOKEN}
    payload = {
        "messaging_product": "whatsapp",
        "reciepient_type": "individual",
        "to": phone_number,
        "type": "text",
        "text": {
            "body": message
        }
    }
    response = requests.post(settings.WHATSAPP_URL,
                             headers=headers, json=payload)
    response_json = response.json()
    return response_json