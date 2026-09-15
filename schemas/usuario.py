from datetime import datetime

from pydantic import BaseModel, EmailStr


class UsuarioWebhook(BaseModel):
    id_formulario: str
    nome: str
    email: EmailStr
    data_resposta: datetime