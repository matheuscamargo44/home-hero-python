from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Telefone(Base):
    __tablename__ = "telefone"
    
    id = Column("tel_id", Integer, primary_key=True, index=True)
    numero_telefone = Column("tel_numero_telefone", String(20), nullable=False)
    tipo_telefone = Column("tel_tipo_telefone", String(20))  # Ex: Celular, Residencial, Comercial
    cliente_id = Column("tel_cli_id", Integer, ForeignKey("cliente.cli_id"))
    prestador_id = Column("tel_pre_id", Integer, ForeignKey("prestador.pre_id"))
    empresa_id = Column("tel_emp_id", Integer, ForeignKey("empresa.emp_id"))
    
    # Relationships
    cliente = relationship("Cliente", back_populates="telefones")
    prestador = relationship("Prestador", back_populates="telefones")
    empresa = relationship("Empresa", back_populates="telefones")

