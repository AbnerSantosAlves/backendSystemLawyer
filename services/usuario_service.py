from models.usuario import Usuario
from schemas.usuario import UsuarioWebhook


class UsuarioService:

    def __init__(self, repository):
        self.repository = repository

    def processar_webhook(
        self,
        dados: UsuarioWebhook
    ):

        usuario_existente = (
            self.repository
            .buscar_por_id_formulario(
                dados.id_formulario
            )
        )

        if usuario_existente:
            return usuario_existente

        usuario = Usuario(
            id_formulario=dados.id_formulario,
            nome=dados.nome,
            email=dados.email,
            data_resposta=dados.data_resposta
        )

        self.repository.criar(usuario)

        self.repository.commit()

        return usuario