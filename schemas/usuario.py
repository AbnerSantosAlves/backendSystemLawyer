from datetime import date

from pydantic import BaseModel


class UsuarioWebhook(BaseModel):
    id_formulario: str
    nome: str
    nr_rg: str  
    nr_cpf: str
    data_nascimento: date
    estado_civil: str
    ds_profissao: str
    ds_endereco: str   
    nr_telefone: str
    ds_assunto: str