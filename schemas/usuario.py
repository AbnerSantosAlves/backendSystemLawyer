from datetime import datetime

from pydantic import BaseModel


class UsuarioWebhook(BaseModel):
    id_formulario: str
    nome: str
    email: str
    data_resposta: datetime