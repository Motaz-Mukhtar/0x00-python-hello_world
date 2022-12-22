#!/usr/bin/python3
""" Containes the class definition of a State and an instance
Base = declarative_base():
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """ Define State that inherits from Base

        id (int): represents a column of an auto-generated,
                    unique integer can't be null and is
                    primary key
        name (string): represents a column of a string
                        maximum 128 characters and can't
                        be null
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
