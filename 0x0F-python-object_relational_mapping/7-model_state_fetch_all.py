#!/usr/bin/python3
"""
a script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]),
            )

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()

    query = session.query(State).order_by(State.id).all()

    for row in query:
        print(f"{row.id}: {row.name}")

    session.close()
