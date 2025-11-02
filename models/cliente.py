from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Cliente(Base):
    __tablename__ = "cliente"
    
    id = Column("cli_id", Integer, primary_key=True, index=True)
    nome_completo = Column("cli_nome_completo", String(80), nullable=False)
    cpf = Column("cli_cpf", String(14), unique=True)
    data_nascimento = Column("cli_data_nascimento", Date)
    forma_pagamento_preferida = Column("cli_forma_pagamento_preferida", String(20))
    senha = Column("cli_senha", String(60))
    endereco_id = Column("cli_endereco_id", Integer, ForeignKey("endereco.end_id"))
    
    # Relationships
    endereco = relationship("Endereco", back_populates="clientes")
    emails = relationship("Email", back_populates="cliente", cascade="all, delete-orphan")
    telefones = relationship("Telefone", back_populates="cliente", cascade="all, delete-orphan")
    agendamentos = relationship("AgendamentoServico", back_populates="cliente", cascade="all, delete-orphan")
    registros_regiao = relationship("RegistroRegiao", back_populates="cliente", cascade="all, delete-orphan")
    avaliacoes = relationship("Avaliacao", back_populates="cliente", cascade="all, delete-orphan")
    notificacoes = relationship("Notificacao", back_populates="cliente", cascade="all, delete-orphan")
    disputas = relationship("DisputaReembolso", back_populates="cliente", cascade="all, delete-orphan")

