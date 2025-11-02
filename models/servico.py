from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Servico(Base):
    __tablename__ = "servico"
    
    id = Column("ser_id", Integer, primary_key=True, index=True)
    nome = Column("ser_nome", String(80), nullable=False)
    descricao = Column("ser_descricao", String(255))
    preco_base = Column("ser_preco_base", Float)
    ativo = Column("ser_ativo", Boolean, default=True)
    categoria_id = Column("ser_cat_id", Integer, ForeignKey("categoria_servico.cat_id"), nullable=False)
    
    # Relationships
    categoria = relationship("CategoriaServico", back_populates="servicos")
    prestadores_servicos = relationship("PrestadorServico", back_populates="servico", cascade="all, delete-orphan")
    empresas_servicos = relationship("EmpresaServico", back_populates="servico", cascade="all, delete-orphan")
    agendamentos = relationship("AgendamentoServico", back_populates="servico", cascade="all, delete-orphan")

