import json
from google import genai
from app.config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


def carregar_prompt():

    with open(
        "app/prompts/atendimento_prompt.txt",
        "r",
        encoding="utf-8"
    ) as f:

        return f.read()


async def processar_audio(audio_path):

    prompt = carregar_prompt()

    uploaded_file = client.files.upload(
        file=audio_path
    )

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=[
            uploaded_file,
            prompt
        ]
    )

    texto = response.text.strip()

    texto = texto.replace("```json", "")
    texto = texto.replace("```", "")

    return json.loads(texto)