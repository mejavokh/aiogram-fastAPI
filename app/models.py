from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class Author(Base):
    __tablename__ = "authors"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(Integer, index=True)
    image = Column(String)

class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    summary = Column(String)
    image = Column(String)
    author_id = Column(Integer, ForeignKey("authors.id"))
    
    author = relationship("Author")