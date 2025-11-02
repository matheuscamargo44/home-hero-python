from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Prestador(Base):
    __tablename__ = "prestador"
    
    id = Column("pre_id", Integer, primary_key=True, index=True)
    nome_completo = Column("pre_nome_completo", String(80), nullable=False)
    cpf = Column("pre_cpf", String(14), unique=True)
    data_nascimento = Column("pre_data_nascimento", Date)
    areas_atuacao = Column("pre_areas_atuacao", String(120))
    experiencia = Column("pre_experiencia", String(255))
    certificados = Column("pre_certificados", String(255))
    senha = Column("pre_senha", String(60))
    endereco_id = Column("pre_endereco_id", Integer, ForeignKey("endereco.end_id"))
    
    # Relationships
    endereco = relationship("Endereco", back_populates="prestadores")
    emails = relationship("Email", back_populates="prestador", cascade="all, delete-orphan")
    telefones = relationship("Telefone", back_populates="prestador", cascade="all, delete-orphan")
    agendamentos = relationship("AgendamentoServico", back_populates="prestador", cascade="all, delete-orphan")
    registros_regiao = relationship("RegistroRegiao", back_populates="prestador", cascade="all, delete-orphan")
    prestadores_servicos = relationship("PrestadorServico", back_populates="prestador", cascade="all, delete-orphan")
    certificacoes = relationship("CertificacaoPrestador", back_populates="prestador", cascade="all, delete-orphan")
    disponibilidades = relationship("DisponibilidadePrestador", back_populates="prestador", cascade="all, delete-orphan")
    avaliacoes = relationship("Avaliacao", back_populates="prestador", cascade="all, delete-orphan")
    notificacoes = relationship("Notificacao", back_populates="prestador", cascade="all, delete-orphan")
    disputas = relationship("DisputaReembolso", back_populates="prestador", cascade="all, delete-orphan")

