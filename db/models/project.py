from sqlalchemy import Column, Integer, String, Text, ARRAY, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Project(Base):
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    title = Column(String(30))
    image_path = Column(String(50))
    summary = Column(String(1200))
    tags = Column(ARRAY(String))

    class Config:
        orm_mode = True


class Document(Base):
    __tablename__ = 'documents'
    id = Column(Integer, primary_key=True)
    project_id = Column(String(30))
    image_path = Column(String(50))
    summary = Column(String(1200))
    tags = Column(ARRAY(String))

    class Config:
        orm_mode = True
