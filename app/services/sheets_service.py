import json
import tempfile
import gspread

from oauth2client.service_account import (
    ServiceAccountCredentials
)

from app.config import (
    GOOGLE_CREDENTIALS_JSON,
    GOOGLE_SHEETS_NAME
)

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

credentials_dict = json.loads(
    GOOGLE_CREDENTIALS_JSON
)

with tempfile.NamedTemporaryFile(
    mode="w",
    delete=False,
    suffix=".json"
) as temp_file:

    json.dump(credentials_dict, temp_file)

    temp_credentials_path = temp_file.name

creds = ServiceAccountCredentials.from_json_keyfile_name(
    temp_credentials_path,
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
        atendimento.get("semana"),
        atendimento.get("dia_semana"),
        atendimento.get("chamado"),
        atendimento.get("tipo_atendimento"),
        ##atendimento.get("colaborador_ti"),
        "Ueslei/SETSIS",
        atendimento.get("descricao"),
        atendimento.get("setor"),
        atendimento.get("quem_ligou"),
        atendimento.get("telefone")
    ])

