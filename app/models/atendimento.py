from pydantic import BaseModel
from typing import Optional

class Atendimento(BaseModel):
    data: Optional[str] = None
    hora_inicio: Optional[str] = None
    hora_fim: Optional[str] = None
    duracao_minutos: Optional[int] = None
    descricao: Optional[str] = None
    telefone: Optional[str] = None
    setor: Optional[str] = None
    quem_ligou: Optional[str] = None