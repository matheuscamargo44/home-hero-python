from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Email(Base):
    __tablename__ = "email"
    
    id = Column("ema_id", Integer, primary_key=True, index=True)
    endereco_email = Column("ema_endereco_email", String(120), nullable=False)
    cliente_id = Column("ema_cli_id", Integer, ForeignKey("cliente.cli_id"))
    prestador_id = Column("ema_pre_id", Integer, ForeignKey("prestador.pre_id"))
    empresa_id = Column("ema_emp_id", Integer, ForeignKey("empresa.emp_id"))
    
    # Relationships
    cliente = relationship("Cliente", back_populates="emails")
    prestador = relationship("Prestador", back_populates="emails")
    empresa = relationship("Empresa", back_populates="emails")

