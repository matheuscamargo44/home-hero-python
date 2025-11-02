from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class DisputaReembolso(Base):
    __tablename__ = "disputa_reembolso"
    
    id = Column("dsp_id", Integer, primary_key=True, index=True)
    agendamento_id = Column("dsp_age_id", Integer, ForeignKey("agendamento_servico.age_id"), nullable=False)
    cliente_id = Column("dsp_cli_id", Integer, ForeignKey("cliente.cli_id"))
    prestador_id = Column("dsp_pre_id", Integer, ForeignKey("prestador.pre_id"))
    motivo = Column("dsp_motivo", String(255))
    status = Column("dsp_status", String(20))  # Ex: Aberta, Em Mediação, Resolvida
    valor_reembolsar = Column("dsp_valor_reembolsar", Float)
    data_abertura = Column("dsp_data_abertura", Date)
    data_fechamento = Column("dsp_data_fechamento", Date)
    
    # Relationships
    agendamento = relationship("AgendamentoServico", back_populates="disputas")
    cliente = relationship("Cliente", back_populates="disputas")
    prestador = relationship("Prestador", back_populates="disputas")

