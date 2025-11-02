from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class ChatbotLog(Base):
    __tablename__ = "chatbot_log"
    
    id = Column("cbt_id", Integer, primary_key=True, index=True)
    cliente_id = Column("cbt_cli_id", Integer, ForeignKey("cliente.cli_id"))
    prestador_id = Column("cbt_pre_id", Integer, ForeignKey("prestador.pre_id"))
    empresa_id = Column("cbt_emp_id", Integer, ForeignKey("empresa.emp_id"))
    agendamento_id = Column("cbt_age_id", Integer, ForeignKey("agendamento_servico.age_id"))
    pergunta = Column("cbt_pergunta", String(300))
    resposta = Column("cbt_resposta", String(500))
    data = Column("cbt_data", Date)
    
    # Relationships
    cliente = relationship("Cliente")
    prestador = relationship("Prestador")
    empresa = relationship("Empresa")
    agendamento = relationship("AgendamentoServico", back_populates="chatbot_logs")

