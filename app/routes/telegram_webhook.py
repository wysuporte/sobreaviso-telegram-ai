from fastapi import APIRouter, Request
from datetime import datetime
from app.services.audio_service import baixar_audio
from app.services.gemini_service import processar_audio
from app.services.time_service import processar_horarios
from app.services.sheets_service import salvar_atendimento
from app.services.telegram_service import enviar_mensagem

router = APIRouter()


@router.post("/webhook")
async def telegram_webhook(request: Request):

    data = await request.json()

    message = data.get("message")

    if not message:
        return {"status": "ignored"}

    chat_id = message["chat"]["id"]

    if "voice" not in message:

        enviar_mensagem(
            chat_id,
            "Envie um áudio para registrar atendimento."
        )

        return {"status": "ignored"}

    file_id = message["voice"]["file_id"]

    try:

        audio_path = baixar_audio(file_id)

        atendimento = await processar_audio(audio_path)

        if not atendimento.get("data"):
            atendimento["data"] = datetime.now().strftime(
                "%d/%m/%Y"
            )

        hora_inicio, hora_fim = processar_horarios(
            atendimento.get("hora_inicio"),
            atendimento.get("hora_fim"),
            atendimento.get("duracao_minutos")
        )

        atendimento["hora_inicio"] = hora_inicio
        atendimento["hora_fim"] = hora_fim

        salvar_atendimento(atendimento)

        mensagem = (
            f"✅ SobreAviso registrado\n\n"
            f"👤 Nome: {atendimento.get('quem_ligou')}\n"
            f"🏥 Setor: {atendimento.get('setor')}\n"
            f"☎️ Fone/Ramal: {atendimento.get('telefone')}\n"
            f"🕒 Tempo: {hora_inicio} às {hora_fim}"
        )

        enviar_mensagem(chat_id, mensagem)

        return {"status": "success"}

    except Exception as e:

        enviar_mensagem(
            chat_id,
            f"Erro ao processar áudio: {str(e)}"
        )

        return {
            "status": "error",
            "message": str(e)
        }