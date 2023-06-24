#!/usr/bin/python3
"""
This script prints all City objects
from the database `hbtn_0e_14_usa`.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    """prevents code execution on import"""
    engine = create('mysql+mysqldb://{}:{}@localhost:3306/{}'
                    .format(argv[1], argv[2], argv[3]))
    
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    stateCal = State(name='California')
    citySF = City(name='San Francisco')
    stateCal.cities.append(CitySF)

    session.add(stateCal)
    session.commit()
    session.close()
