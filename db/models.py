from sqlalchemy import Column, Integer, String, Text, ARRAY
from database import Base, engine


class Project(Base):
    __tablename__ = 'project'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30))
    image_path = Column(String(50))
    summary = Column(String(1200))
    tags = Column(ARRAY(String))
    
    class Config:
        orm_mode = True




Base.metadata.create_all(engine)