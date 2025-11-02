from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Empresa(Base):
    __tablename__ = "empresa"
    
    id = Column("emp_id", Integer, primary_key=True, index=True)
    razao_social = Column("emp_razao_social", String(120), nullable=False)
    cnpj = Column("emp_cnpj", String(18), unique=True)
    area_atuacao = Column("emp_area_atuacao", String(120))
    representante_responsavel = Column("emp_representante_responsavel", String(80))
    senha = Column("emp_senha", String(60))
    endereco_id = Column("emp_endereco_id", Integer, ForeignKey("endereco.end_id"))
    
    # Relationships
    endereco = relationship("Endereco", back_populates="empresas")
    emails = relationship("Email", back_populates="empresa", cascade="all, delete-orphan")
    telefones = relationship("Telefone", back_populates="empresa", cascade="all, delete-orphan")
    agendamentos = relationship("AgendamentoServico", back_populates="empresa", cascade="all, delete-orphan")
    funcionarios = relationship("FuncionarioEmpresa", back_populates="empresa", cascade="all, delete-orphan")
    registros_regiao = relationship("RegistroRegiao", back_populates="empresa", cascade="all, delete-orphan")
    empresas_servicos = relationship("EmpresaServico", back_populates="empresa", cascade="all, delete-orphan")
    avaliacoes = relationship("Avaliacao", back_populates="empresa", cascade="all, delete-orphan")
    notificacoes = relationship("Notificacao", back_populates="empresa", cascade="all, delete-orphan")
    chatbot_logs = relationship("ChatbotLog", back_populates="empresa", cascade="all, delete-orphan")

