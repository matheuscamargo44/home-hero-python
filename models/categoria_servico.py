from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class CategoriaServico(Base):
    __tablename__ = "categoria_servico"
    
    id = Column("cat_id", Integer, primary_key=True, index=True)
    nome = Column("cat_nome", String(60), nullable=False)
    descricao = Column("cat_descricao", String(255))
    
    # Relationships
    servicos = relationship("Servico", back_populates="categoria", cascade="all, delete-orphan")

