from sqlalchemy import Column, Integer, Date, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class EmpresaServico(Base):
    __tablename__ = "empresa_servico"
    
    id = Column("ems_id", Integer, primary_key=True, index=True)
    empresa_id = Column("ems_emp_id", Integer, ForeignKey("empresa.emp_id"), nullable=False)
    servico_id = Column("ems_ser_id", Integer, ForeignKey("servico.ser_id"), nullable=False)
    preco_oferta = Column("ems_preco_oferta", Float)
    ativo = Column("ems_ativo", Boolean, default=True)
    data_cadastro = Column("ems_data_cadastro", Date)
    
    # Relationships
    empresa = relationship("Empresa", back_populates="empresas_servicos")
    servico = relationship("Servico", back_populates="empresas_servicos")

