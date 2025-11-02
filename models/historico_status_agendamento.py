from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class HistoricoStatusAgendamento(Base):
    __tablename__ = "historico_status_agendamento"
    
    id = Column("his_id", Integer, primary_key=True, index=True)
    agendamento_id = Column("his_age_id", Integer, ForeignKey("agendamento_servico.age_id"), nullable=False)
    status_anterior = Column("his_status_anterior", String(20))
    status_novo = Column("his_status_novo", String(20))
    data_alteracao = Column("his_data_alteracao", Date)
    
    # Relationships
    agendamento = relationship("AgendamentoServico", back_populates="historicos_status")

