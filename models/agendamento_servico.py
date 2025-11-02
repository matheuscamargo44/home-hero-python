from sqlalchemy import Column, Integer, String, Date, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import event
from datetime import date
from database import Base

class AgendamentoServico(Base):
    __tablename__ = "agendamento_servico"
    
    id = Column("age_id", Integer, primary_key=True, index=True)
    cliente_id = Column("age_cli_id", Integer, ForeignKey("cliente.cli_id"), nullable=False)
    servico_id = Column("age_ser_id", Integer, ForeignKey("servico.ser_id"), nullable=False)
    prestador_id = Column("age_pre_id", Integer, ForeignKey("prestador.pre_id"))
    empresa_id = Column("age_emp_id", Integer, ForeignKey("empresa.emp_id"))
    data = Column("age_data", Date)
    janela = Column("age_janela", String(20))
    endereco_id = Column("age_end_id", Integer, ForeignKey("endereco.end_id"))
    status = Column("age_status", String(20))
    valor = Column("age_valor", Float)
    pago = Column("age_pago", Boolean, default=False)
    data_cancelamento = Column("age_data_cancelamento", Date)
    motivo_cancelamento = Column("age_motivo_cancelamento", String(120))
    
    # Relationships
    cliente = relationship("Cliente", back_populates="agendamentos")
    servico = relationship("Servico", back_populates="agendamentos")
    prestador = relationship("Prestador", back_populates="agendamentos")
    empresa = relationship("Empresa", back_populates="agendamentos")
    endereco = relationship("Endereco")
    historicos_status = relationship("HistoricoStatusAgendamento", back_populates="agendamento", cascade="all, delete-orphan")
    atribuicoes = relationship("AtribuicaoServico", back_populates="agendamento", cascade="all, delete-orphan")
    pagamentos = relationship("Pagamento", back_populates="agendamento", cascade="all, delete-orphan")
    disputas = relationship("DisputaReembolso", back_populates="agendamento", cascade="all, delete-orphan")
    avaliacoes = relationship("Avaliacao", back_populates="agendamento", cascade="all, delete-orphan")
    chat_mensagens = relationship("ChatMensagem", back_populates="agendamento", cascade="all, delete-orphan")
    chatbot_logs = relationship("ChatbotLog", back_populates="agendamento", cascade="all, delete-orphan")

# Event listeners equivalent to Java @PostPersist and @PostUpdate
@event.listens_for(AgendamentoServico, 'after_insert')
def after_insert_agendamento(mapper, connection, target):
    """Equivalente ao @PostPersist do Java"""
    from .historico_status_agendamento import HistoricoStatusAgendamento
    historico_table = HistoricoStatusAgendamento.__table__
    connection.execute(
        historico_table.insert().values(
            agendamento_id=target.id,
            status_anterior="Criado",
            status_novo=target.status if target.status else "Pendente",
            data_alteracao=date.today()
        )
    )

@event.listens_for(AgendamentoServico, 'before_update')
def before_update_agendamento(mapper, connection, target):
    """Armazena status anterior antes da atualização"""
    from sqlalchemy import inspect
    insp = inspect(target)
    # Obter valor anterior do status usando get_history
    history = insp.get_history('status', True)
    if history.has_changes() and history.deleted:
        target._status_anterior = history.deleted[0]

@event.listens_for(AgendamentoServico, 'after_update')
def after_update_agendamento(mapper, connection, target):
    """Equivalente ao @PostUpdate do Java"""
    from .historico_status_agendamento import HistoricoStatusAgendamento
    status_anterior = getattr(target, '_status_anterior', None)
    
    # Verificar se o status mudou
    if status_anterior and status_anterior != target.status:
        historico_table = HistoricoStatusAgendamento.__table__
        connection.execute(
            historico_table.insert().values(
                agendamento_id=target.id,
                status_anterior=status_anterior,
                status_novo=target.status,
                data_alteracao=date.today()
            )
        )

