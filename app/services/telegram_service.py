import requests
from app.config import TELEGRAM_TOKEN


def enviar_mensagem(chat_id, texto):

    url = (
        f"https://api.telegram.org/bot"
        f"{TELEGRAM_TOKEN}/sendMessage"
    )

    payload = {
        "chat_id": chat_id,
        "text": texto
    }

    requests.post(url, json=payload)