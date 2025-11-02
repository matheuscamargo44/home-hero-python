from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class ChatMensagem(Base):
    __tablename__ = "chat_mensagem"
    
    id = Column("cha_id", Integer, primary_key=True, index=True)
    agendamento_id = Column("cha_age_id", Integer, ForeignKey("agendamento_servico.age_id"))
    remetente_tipo = Column("cha_remetente_tipo", String(20))
    remetente_id = Column("cha_remetente_id", Integer)
    destinatario_tipo = Column("cha_destinatario_tipo", String(20))
    destinatario_id = Column("cha_destinatario_id", Integer)
    mensagem = Column("cha_mensagem", String(500))
    data = Column("cha_data", Date)
    
    # Relationships
    agendamento = relationship("AgendamentoServico", back_populates="chat_mensagens")

