from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.session import get_db
from repositories.usuario_repositorio import UsuarioRepository
from schemas.usuario import UsuarioWebhook
from services.usuario_service import UsuarioService


router = APIRouter(
    prefix="/webhooks",
    tags=["Webhooks"]
)


@router.post("/formulario")
def receber_formulario(
    dados: UsuarioWebhook,
    db: Session = Depends(get_db)
):

    repository = UsuarioRepository(db)

    service = UsuarioService(repository)

    usuario = service.processar_webhook(dados)

    return {
        "message": "Usuário processado",
        "usuario_id": usuario.id
    }
    
@router.get("/usuarios")
def getAllUser(
    db: Session = Depends(get_db)
):
    repository = UsuarioRepository(db)

    return repository.getAllUser()