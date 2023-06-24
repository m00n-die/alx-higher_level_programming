#!/usr/bin/python3
"""prints all City objects"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                            .format(sys.argv[1], sys.argv[2],
                                    sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    stmt = session.query(City, State).join(State)
    for _c, _s, in stmt.all():
        print("{}: ({:d}) {}".format(_s.name, _c.id, _c.name))
    session.commit()
    session.close()
