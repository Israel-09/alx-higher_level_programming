#!/usr/bin/python3
'''fetches all rows'''
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    session = Session(engine)

    #  inserts new row to the table
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    print('{}'.format(new_state.id))
    session.close()
