#!/usr/bin/python3
"""
Script that create a new state table and connect to localhost using port 3306.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base


Base = declarative_base()


class State(Base):
    """
    The state class that inherits from Base.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          back_populates="state", cascade="all, delete",
                          order_by="City.id")
