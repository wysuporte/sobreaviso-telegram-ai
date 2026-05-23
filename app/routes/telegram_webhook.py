from fastapi import APIRouter, Request
from datetime import datetime
import logging
import os

from app.services.audio_service import baixar_audio
from app.services.gemini_service import processar_audio
from app.services.time_service import processar_horarios
from app.services.sheets_service import salvar_atendimento
from app.services.telegram_service import enviar_mensagem

router = APIRouter()

# Usuários autorizados
USUARIOS_AUTORIZADOS = [
    "776933548"
]


@router.post("/webhook")
async def telegram_webhook(request: Request):

    logging.info("Webhook recebido")

    audio_path = None
    chat_id = None

    try:

        data = await request.json()

        message = data.get("message")

        if not message:

            logging.warning(
                "Mensagem inválida recebida"
            )

            return {"status": "ignored"}

        chat_id = message["chat"]["id"]

        telegram_user = message["from"]

        telegram_user_id = str(
            telegram_user.get("id")
        )

        telegram_username = (
            telegram_user.get("username")
        )

        telegram_nome = (
            telegram_user.get("first_name")
        )

        logging.info(
            f"Mensagem recebida "
            f"chat_id={chat_id} "
            f"user={telegram_username}"
        )

        # Validação usuário autorizado
        if telegram_user_id not in USUARIOS_AUTORIZADOS:

            logging.warning(
                f"Usuário não autorizado: "
                f"{telegram_user_id}"
            )

            enviar_mensagem(
                chat_id,
                "Usuário não autorizado."
            )

            return {
                "status": "unauthorized"
            }

        # Validar áudio
        if "voice" not in message:

            logging.warning(
                "Mensagem sem áudio"
            )

            enviar_mensagem(
                chat_id,
                "Envie um áudio para registrar atendimento."
            )

            return {"status": "ignored"}

        file_id = message["voice"]["file_id"]

        logging.info(
            f"Download áudio iniciado "
            f"file_id={file_id}"
        )

        # Download áudio
        audio_path = baixar_audio(file_id)

        logging.info(
            f"Áudio salvo: {audio_path}"
        )

        # Processar Gemini
        atendimento = await processar_audio(
            audio_path
        )

        if not isinstance(atendimento, dict):
            raise ValueError(
                "Gemini retornou formato inválido"
            )

        logging.info(
            "Áudio processado pelo Gemini"
        )

        # Adicionar informações Telegram
        atendimento["telegram_id"] = (
            telegram_user_id
        )

        atendimento["telegram_username"] = (
            telegram_username
        )

        atendimento["usuario_nome"] = (
            telegram_nome
        )

        # Fallback data
        if not atendimento.get("data"):

            atendimento["data"] = (
                datetime.now().strftime(
                    "%d/%m/%Y"
                )
            )

        # Processar horários
        hora_inicio, hora_fim = (
            processar_horarios(
                atendimento.get("hora_inicio"),
                atendimento.get("hora_fim"),
                atendimento.get(
                    "duracao_minutos"
                )
            )
        )

        atendimento["hora_inicio"] = (
            hora_inicio
        )

        atendimento["hora_fim"] = (
            hora_fim
        )

        logging.info(
            "Salvando atendimento no Sheets"
        )

        # Salvar Sheets
        salvar_atendimento(atendimento)

        logging.info(
            "Atendimento registrado "
            "com sucesso"
        )

        # Mensagem retorno
        mensagem = (
            f"✅ SobreAviso registrado\n\n"
            f"👤 Nome: "
            f"{atendimento.get('quem_ligou')}\n"
            f"🏥 Setor: "
            f"{atendimento.get('setor')}\n"
            f"☎️ Fone/Ramal: "
            f"{atendimento.get('telefone')}\n"
            f"🕒 Tempo: "
            f"{hora_inicio} às {hora_fim}"
        )

        enviar_mensagem(chat_id, mensagem)

        return {"status": "success"}


    except Exception as e:

        erro_msg = str(e)

        logging.exception(

            "Erro ao processar áudio"

        )

        try:

            if chat_id:
                enviar_mensagem(

                    chat_id,

                    f"Erro ao processar áudio: "

                    f"{erro_msg}"

                )


        except Exception:

            logging.exception(

                "Erro ao enviar mensagem "

                "Telegram"

            )

        return {

            "status": "error",

            "message": erro_msg

        }

    finally:

        # Remover áudio temporário
        if (
            audio_path
            and os.path.exists(audio_path)
        ):

            os.remove(audio_path)

            logging.info(
                f"Áudio removido: "
                f"{audio_path}"
            )