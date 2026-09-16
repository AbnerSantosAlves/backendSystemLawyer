from sqlalchemy import String, LargeBinary, Date
from sqlalchemy.orm import Mapped, mapped_column

from database.session import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(
        primary_key=True
    )

    id_formulario: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    nome: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    nr_cpf: Mapped[str] = mapped_column(
        String(11),
        nullable=False
    )
    
    data_nascimento: Mapped[Date] = mapped_column(
        Date,
        nullable=False
    )
    
    estado_civil: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    
    ds_profissao: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    nr_telefone: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )
    
    ds_assunto: Mapped[str] = mapped_column(
        String(150),
        nullable=False
    )
    
    documento = Mapped[bytes] = mapped_column(
        LargeBinary,
        nullable=False
    )
    
    documento_nome = Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )