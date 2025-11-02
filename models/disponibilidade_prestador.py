from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class DisponibilidadePrestador(Base):
    __tablename__ = "disponibilidade_prestador"
    
    id = Column("dis_id", Integer, primary_key=True, index=True)
    prestador_id = Column("dis_pre_id", Integer, ForeignKey("prestador.pre_id"), nullable=False)
    dia_semana = Column("dis_dia_semana", String(10))  # Ex: Segunda, Terça, etc.
    janela = Column("dis_janela", String(20))  # Ex: Manhã, Tarde, Noite, 08:00-12:00
    ativo = Column("dis_ativo", Boolean, default=True)
    
    # Relationships
    prestador = relationship("Prestador", back_populates="disponibilidades")

