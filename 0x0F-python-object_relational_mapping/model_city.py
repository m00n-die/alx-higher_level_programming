#!/usr/bin/python3
"""contains the class definition of a City"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """defines the city class"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=Fallse)
    state_id = Column(Integer, ForeignKey('stated.id'), nullable=False)
