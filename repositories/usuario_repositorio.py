from sqlalchemy import select
from sqlalchemy.orm import Session

from models.usuario import Usuario


class UsuarioRepository:

    def __init__(self, db: Session):
        self.db = db


    def getAllUser(
        self
    ):
        # 1. Cria a query com select()
        query = select(Usuario)
    
         # 2. Executa usando scalars() para retornar a lista de objetos limpa
        usuarios = self.db.scalars(query).all()
        return usuarios
    
    def buscar_por_id_formulario(
        self,
        id_formulario: str
    ):
        statement = select(Usuario).where(
            Usuario.id_formulario == id_formulario
        )

        return self.db.scalar(statement)

    def criar(
        self,
        usuario: Usuario
    ):
        self.db.add(usuario)

    def commit(self):
        self.db.commit()

    def rollback(self):
        self.db.rollback()