#!/usr/bin/python3

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                       .format(sys.argv[1], sys.argv[2],
                               sys.argv[3]), pool_pre_ping=True)

Session = sessionmaker(bind=engine)
session = Session()

for value in session.query(State).ordery_by(State.id).filter(...).first():
    print('{}: {}'.format(value.id, value.name))
