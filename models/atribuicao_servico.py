from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class AtribuicaoServico(Base):
    __tablename__ = "atribuicao_servico"
    
    id = Column("atr_id", Integer, primary_key=True, index=True)
    agendamento_id = Column("atr_age_id", Integer, ForeignKey("agendamento_servico.age_id"), nullable=False)
    funcionario_id = Column("atr_fun_id", Integer, ForeignKey("funcionario_empresa.fun_id"), nullable=False)
    data = Column("atr_data", Date)
    status = Column("atr_status", String(20))  # Ex: Atribuído, Aceito, Recusado, Concluído
    
    # Relationships
    agendamento = relationship("AgendamentoServico", back_populates="atribuicoes")
    funcionario = relationship("FuncionarioEmpresa", back_populates="atribuicoes")

