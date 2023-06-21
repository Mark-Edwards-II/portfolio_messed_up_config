from sqlalchemy import Column, Integer, String, Text, ARRAY, ForeignKey, ForeignKeyConstraint, TIMESTAMP, func
from typing import List

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


class Base(DeclarativeBase):
    pass
# Base = declarative_base()

class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(30))
    summary = Column(String(1200))
    tags:Column = Column(ARRAY(String))
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_onupdate=func.now())
    # child: Mapped["Document"] = relationship(back_populates="parent")
    class Config:
        orm_mode = True

    def __repr__(self):
        return f"{self.__class__.__qualname__} title={self.title}"

# class Document(Base):
#     __tablename__ = 'documents'
#     id = Column(Integer, primary_key=True)
#     project_id = ForeignKey()
#     title = Column(String(30))
#     image_path = Column(String(50))
#     summary = Column(String(1200))
#     tags = Column(ARRAY(String))
#     parent_id: Mapped[int] = mapped_column(ForeignKey("parent_table.id"))
#     parent: Mapped["Project"] = relationship(back_populates="child")

#     class Config:
#         orm_mode = True
    
#     def __repr__(self):
#         return f"{self.__class__.__qualname__} title={self.title}"

# class Document(Base):
#     __tablename__ = 'documents'
#     id = Column(Integer, primary_key=True)
#     project_id = ForeignKey()
#     image_path = Column(String(50))
#     summary = Column(String(1200))
#     tags = Column(ARRAY(String))

#     class Config:
#         orm_mode = True

# Base.metadata.create_all(engine)