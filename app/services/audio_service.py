import os
import requests
from app.config import TELEGRAM_TOKEN


def baixar_audio(file_id):

    file_url = (
        f"https://api.telegram.org/bot"
        f"{TELEGRAM_TOKEN}/getFile?file_id={file_id}"
    )

    response = requests.get(file_url).json()

    file_path = response["result"]["file_path"]

    download_url = (
        f"https://api.telegram.org/file/bot"
        f"{TELEGRAM_TOKEN}/{file_path}"
    )

    os.makedirs("audios", exist_ok=True)

    local_path = f"audios/{file_id}.ogg"

    audio_data = requests.get(download_url)

    with open(local_path, "wb") as f:
        f.write(audio_data.content)

    return local_path