from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class Regiao(Base):
    __tablename__ = "regiao"
    
    id = Column("reg_id", Integer, primary_key=True, index=True)
    nome = Column("reg_nome", String(80), nullable=False)
    cidade = Column("reg_cidade", String(60))
    uf = Column("reg_uf", String(2))
    
    # Relationships
    registros = relationship("RegistroRegiao", back_populates="regiao", cascade="all, delete-orphan")

