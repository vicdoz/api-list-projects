from infraestructure.user.model.user import User

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = Base.metadata


class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(250), nullable=False, unique=True)
    url = Column(String(250), nullable=True)
    owner_id = Column(ForeignKey('user.id'))
    owner = relationship("User", back_populates="projects")
