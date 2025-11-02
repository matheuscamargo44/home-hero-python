from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class RegistroRegiao(Base):
    __tablename__ = "registro_regiao"
    
    id = Column("rre_id", Integer, primary_key=True, index=True)
    regiao_id = Column("rre_reg_id", Integer, ForeignKey("regiao.reg_id"), nullable=False)
    cliente_id = Column("rre_cli_id", Integer, ForeignKey("cliente.cli_id"))
    prestador_id = Column("rre_pre_id", Integer, ForeignKey("prestador.pre_id"))
    empresa_id = Column("rre_emp_id", Integer, ForeignKey("empresa.emp_id"))
    data_registro = Column("rre_data_registro", Date)
    
    # Relationships
    regiao = relationship("Regiao", back_populates="registros")
    cliente = relationship("Cliente", back_populates="registros_regiao")
    prestador = relationship("Prestador", back_populates="registros_regiao")
    empresa = relationship("Empresa", back_populates="registros_regiao")

