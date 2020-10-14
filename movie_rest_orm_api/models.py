"""
model.py : database row <-> objet python
"""
from sqlalchemy import Column, Integer, String, SmallInteger, Date, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=250), nullable=False)
    year = Column(SmallInteger, nullable=False)
    duration = Column(SmallInteger, nullable=True)
    # Many to one relationship : director
    id_director = Column(Integer, ForeignKey('stars.id'))
    director = relationship('Star')


class Star(Base):
    __tablename__ = "stars"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=150), nullable=False)
    birthdate = Column(Date, nullable=True)
