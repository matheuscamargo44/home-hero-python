from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Endereco(Base):
    __tablename__ = "endereco"
    
    id = Column("end_id", Integer, primary_key=True, index=True)
    logradouro = Column("end_logradouro", String(100))
    numero = Column("end_numero", String(15))
    complemento = Column("end_complemento", String(60))
    bairro = Column("end_bairro", String(60))
    cidade = Column("end_cidade", String(60))
    uf = Column("end_uf", String(2))
    cep = Column("end_cep", String(10))
    
    # Relationships
    clientes = relationship("Cliente", back_populates="endereco")
    prestadores = relationship("Prestador", back_populates="endereco")
    empresas = relationship("Empresa", back_populates="endereco")

