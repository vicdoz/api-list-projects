
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)

    projects = relationship("Projects", back_populates="owner")

class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(250), nullable=False, unique=True)
    url = Column(String(250), nullable=True)
    owner_id = Column(ForeignKey('user.id'))
    owner = relationship("User", back_populates="projects")
