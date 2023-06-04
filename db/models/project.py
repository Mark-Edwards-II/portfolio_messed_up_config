from sqlalchemy import Column, Integer, String, Text, ARRAY
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Project(Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True)
    title = Column(String(30))
    image_path = Column(String(50))
    summary = Column(String(1200))
    tags = Column(ARRAY(String))
    
    class Config:
        orm_mode = True




from pydantic import BaseModel, FilePath


class Project(BaseModel):
    """The summary of a Project.
    """
    project_id: int
    title: str
    image: FilePath
    summary: str
    tags: list[str]


class Document(BaseModel):
    """Details documenting the projecit
    """
    document_id: int
    project_id: int
    large_text: str

