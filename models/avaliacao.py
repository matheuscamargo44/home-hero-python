from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import event
from datetime import date
from database import Base
from .notificacao import Notificacao

class Avaliacao(Base):
    __tablename__ = "avaliacao"
    
    id = Column("ava_id", Integer, primary_key=True, index=True)
    agendamento_id = Column("ava_age_id", Integer, ForeignKey("agendamento_servico.age_id"), nullable=False)
    cliente_id = Column("ava_cli_id", Integer, ForeignKey("cliente.cli_id"), nullable=False)
    prestador_id = Column("ava_pre_id", Integer, ForeignKey("prestador.pre_id"), nullable=False)
    nota = Column("ava_nota", Integer)
    comentario = Column("ava_comentario", String(400))
    data = Column("ava_data", Date)
    
    # Relationships
    agendamento = relationship("AgendamentoServico", back_populates="avaliacoes")
    cliente = relationship("Cliente", back_populates="avaliacoes")
    prestador = relationship("Prestador", back_populates="avaliacoes")

# Event listener equivalente ao @PostPersist do Java
@event.listens_for(Avaliacao, 'after_insert')
def after_insert_avaliacao(mapper, connection, target):
    """Equivalente ao @PostPersist do AvaliacaoListener"""
    from .notificacao import Notificacao
    notificacao_table = Notificacao.__table__
    connection.execute(
        notificacao_table.insert().values(
            cliente_id=target.cliente_id,
            prestador_id=target.prestador_id,
            agendamento_id=target.agendamento_id,
            tipo="Avaliacao",
            mensagem="Nova avaliação registrada.",
            enviado=False,
            data=date.today()
        )
    )

