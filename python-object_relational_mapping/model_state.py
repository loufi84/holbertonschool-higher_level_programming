#!/usr/bin/python3
"""
Script that create a new state table and connect to localhost using port 3306.
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import MySQLdb


Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    engine_name = "mysql+pymysql://username:password@localhost:3306/db_name"
    engine = create_engine(engine_name)
    Base.metadata.create_all(engine)
