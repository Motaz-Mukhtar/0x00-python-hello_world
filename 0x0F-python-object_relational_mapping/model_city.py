#!/usr/bin/python3
"""
    Create the City class or Table
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
        Defining City Class:

        id (int): Integer primary_key and
                  can't be NULL
        name (string): String 128 can't be NULL
        state_id (int): Integer can't be NULL and
                        it's foreignkey to states.id
                          ( pool_pre_ping=True)
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
