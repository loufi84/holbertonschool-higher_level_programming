#!/usr/bin/python3
"""
Script that defines the State class with a relationship to City.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base


class State(Base):
    """
    The state class that inherits from Base with a relationship to City.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state",
                          cascade="all, delete")
