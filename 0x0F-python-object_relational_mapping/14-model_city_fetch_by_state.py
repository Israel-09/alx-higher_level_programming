#!/usr/bin/python3
'''fetches all rows'''
import sys
from model_state import Base, City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    
    session = Session(engine)

    for state in session.query(City).order_by(City.id).all():
        print("{}: {} {}".format(state.id, state.name))

    session.close()
