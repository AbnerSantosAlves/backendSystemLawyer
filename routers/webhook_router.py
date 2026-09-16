from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import Response
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
    db: Session = Depends(get_db), response_model=UsuarioWebhook
):
    repository = UsuarioRepository(db)

    return repository.getAllUser()

@router.get("/usuarios/{usuario_id}/documento")
def getDocumento(
    usuario_id: int,
    db: Session = Depends(get_db)
):
    repository = UsuarioRepository(db)

    usuario = repository.buscar_por_id_formulario(usuario_id)

    if not usuario:
        raise HTTPException(
            status_code=404,
            detail="Usuário não encontrado"
        )

    if not usuario.documento:
        raise HTTPException(
            status_code=404,
            detail="Documento não encontrado"
        )

    return Response(
        content=usuario.documento,
        media_type=(
            usuario.documento_tipo
            or "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        ),
        headers={
            "Content-Disposition": (
                f'attachment; filename="{usuario.documento_nome}"'
            )
        }
    )