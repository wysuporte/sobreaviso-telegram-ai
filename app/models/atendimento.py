from pydantic import BaseModel
from typing import Optional

class Atendimento(BaseModel):
    data: Optional[str] = None
    hora_inicio: Optional[str] = None
    hora_fim: Optional[str] = None
    duracao_minutos: Optional[int] = None
    semana: Optional[str] = None
    dia_semana: Optional[str] = None
    chamado: Optional[str] = None
    tipo_atendimento: Optional[str] = None
    colaborador_ti: Optional[str] = None
    descricao: Optional[str] = None
    setor: Optional[str] = None
    quem_ligou: Optional[str] = None
    telefone: Optional[str] = None