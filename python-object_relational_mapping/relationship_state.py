#!/usr/bin/python3
"""module to improve on the file model_state.py"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

# Create a new declarative_base instance called Base
Base = declarative_base()


class State(Base):
    """Class State"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")
