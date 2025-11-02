from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class CertificacaoPrestador(Base):
    __tablename__ = "certificacao_prestador"
    
    id = Column("cer_id", Integer, primary_key=True, index=True)
    prestador_id = Column("cer_pre_id", Integer, ForeignKey("prestador.pre_id"), nullable=False)
    titulo = Column("cer_titulo", String(120))
    instituicao = Column("cer_instituicao", String(120))
    data_conclusao = Column("cer_data_conclusao", Date)
    url = Column("cer_url", String(255))  # URL do arquivo no Cloudinary ou S3
    
    # Relationships
    prestador = relationship("Prestador", back_populates="certificacoes")

