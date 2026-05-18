import gspread
from oauth2client.service_account import ServiceAccountCredentials
from app.config import (
    GOOGLE_CREDENTIALS_FILE,
    GOOGLE_SHEETS_NAME
)

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    GOOGLE_CREDENTIALS_FILE,
    scope
)

client = gspread.authorize(creds)

sheet = client.open(
    GOOGLE_SHEETS_NAME
).sheet1


def salvar_atendimento(atendimento):

    sheet.append_row([
        atendimento.get("data"),
        atendimento.get("hora_inicio"),
        atendimento.get("hora_fim"),
        atendimento.get("duracao_minutos"),
        atendimento.get("descricao"),
        atendimento.get("telefone"),
        atendimento.get("setor"),
        atendimento.get("quem_ligou")
    ])