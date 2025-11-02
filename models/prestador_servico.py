from sqlalchemy import Column, Integer, Date, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class PrestadorServico(Base):
    __tablename__ = "prestador_servico"
    
    id = Column("prs_id", Integer, primary_key=True, index=True)
    prestador_id = Column("prs_pre_id", Integer, ForeignKey("prestador.pre_id"), nullable=False)
    servico_id = Column("prs_ser_id", Integer, ForeignKey("servico.ser_id"), nullable=False)
    preco_oferta = Column("prs_preco_oferta", Float)
    ativo = Column("prs_ativo", Boolean, default=True)
    data_cadastro = Column("prs_data_cadastro", Date)
    
    # Relationships
    prestador = relationship("Prestador", back_populates="prestadores_servicos")
    servico = relationship("Servico", back_populates="prestadores_servicos")

