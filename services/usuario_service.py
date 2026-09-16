from models.usuario import Usuario
from schemas.usuario import UsuarioWebhook
from docModel import criar_documento


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

        contrato = criar_documento(dados)
        usuario = Usuario(
            id_formulario=dados.id_formulario,
            nome=dados.nome,
            nr_cpf=dados.nr_cpf,
            data_nascimento=dados.data_nascimento,
            estado_civil=dados.estado_civil,
            ds_profissao=dados.ds_profissao,
            nr_telefone=dados.nr_telefone,
            ds_assuton=dados.ds_assunto,
            documento=contrato,
            documento=f"documento_{dados.nome}"
        )

        self.repository.criar(usuario)

        self.repository.commit()

        return usuario