#!/usr/bin/python3
"""a python file that contains the class
definition of a State and an
instance Base = declarative_base()"""


from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine("mysql://root:root@localhost/hbtn_0e_6_usa")
Base = declarative_base()


class State(Base):
    """A sate class that defines states"""
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True,
                unique=True, primary_key=True,
                nullable=False)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
