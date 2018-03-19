from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Project(Base):
    __tablename__ = 'project'

    id = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(250), nullable=False, unique=True)
    url = Column(String(250), nullable=True)
    owner = Column(String(250), nullable=False)

