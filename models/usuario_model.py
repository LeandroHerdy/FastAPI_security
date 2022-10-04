from email.policy import default
from operator import index
from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.orm import relationship

from core.configs import settings

class UsuarioModel(settings.DBBaseModel):
    __tablename__= 'usuario'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(256), nullable=True)
    sobrenome = Column(String(256), nullable=True)
    email = Column(String(256), index=True, nullable=False, unique=True)
    senha = Column(String(256), nullable=False)
    eh_admin = Column(Boolean, default=False)
    artigo = relationship("ArtigoModel", cascade="all, delete-orphan", back_populates="criador", uselist=True, lazy="joined")
    