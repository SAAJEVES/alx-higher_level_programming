#!/usr/bin/python3
"""Start link class to table in database
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]),
            pool_pre_ping=True
            )

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()

    if len(sys.argv) != 4:
        exit(1)

    query = session.query(State).order_by(State.id).all()

    for row in query:
        print(f"{row.id}: {row.name}")

    session.close()
