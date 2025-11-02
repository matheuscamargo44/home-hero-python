from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class FuncionarioEmpresa(Base):
    __tablename__ = "funcionario_empresa"
    
    id = Column("fun_id", Integer, primary_key=True, index=True)
    empresa_id = Column("fun_emp_id", Integer, ForeignKey("empresa.emp_id"), nullable=False)
    nome = Column("fun_nome", String(80), nullable=False)
    especialidade = Column("fun_especialidade", String(80))
    ativo = Column("fun_ativo", Boolean, default=True)
    
    # Relationships
    empresa = relationship("Empresa", back_populates="funcionarios")
    atribuicoes = relationship("AtribuicaoServico", back_populates="funcionario", cascade="all, delete-orphan")

