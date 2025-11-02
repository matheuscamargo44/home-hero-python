from sqlalchemy import Column, Integer, String, Date, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Notificacao(Base):
    __tablename__ = "notificacao"
    
    id = Column("not_id", Integer, primary_key=True, index=True)
    cliente_id = Column("not_cli_id", Integer, ForeignKey("cliente.cli_id"))
    prestador_id = Column("not_pre_id", Integer, ForeignKey("prestador.pre_id"))
    empresa_id = Column("not_emp_id", Integer, ForeignKey("empresa.emp_id"))
    agendamento_id = Column("not_age_id", Integer, ForeignKey("agendamento_servico.age_id"))
    tipo = Column("not_tipo", String(30))  # Ex: Confirmação, Lembrete, Cancelamento, Avaliação, Disputa
    mensagem = Column("not_mensagem", String(255))
    enviado = Column("not_enviado", Boolean, default=False)
    data = Column("not_data", Date)
    
    # Relationships
    cliente = relationship("Cliente", back_populates="notificacoes")
    prestador = relationship("Prestador", back_populates="notificacoes")
    empresa = relationship("Empresa", back_populates="notificacoes")
    agendamento = relationship("AgendamentoServico")

