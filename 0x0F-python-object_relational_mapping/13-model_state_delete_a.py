#!/usr/bin/python3
'''
script that deletes all State objects with a name containing
the letter a from the database hbtn_0e_6_usa
'''

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    Base.metadat.create_all(engine)

    with Session() as session:
        query_a = session.query(State).filter(State.name.like('%a%'))
        order_by(State.id)

        for row_a in query_a:
            session.delete(row_a)
