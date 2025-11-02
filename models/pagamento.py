from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Pagamento(Base):
    __tablename__ = "pagamento"
    
    id = Column("pag_id", Integer, primary_key=True, index=True)
    agendamento_id = Column("pag_age_id", Integer, ForeignKey("agendamento_servico.age_id"), nullable=False)
    forma = Column("pag_forma", String(20))  # Ex: Cartão Crédito, Cartão Débito, PIX, Boleto
    valor_total = Column("pag_valor_total", Float)
    status = Column("pag_status", String(20))  # Ex: Pendente, Pago, Recusado, Reembolsado
    referencia_gateway = Column("pag_referencia_gateway", String(60))  # ID da transação no gateway externo
    data = Column("pag_data", Date)
    
    # Relationships
    agendamento = relationship("AgendamentoServico", back_populates="pagamentos")

