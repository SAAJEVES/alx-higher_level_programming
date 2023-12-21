#!/usr/bin/python3
'''
script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
'''

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":

    if len(sys.argv) != 5:
        sys.exit(1)

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    search = sys.argv[4]

    with Session() as session:
        query_name = session.query(State).filter(State.name.like(search)).one()

        if query_name:
            print(query_name.id)
        else:
            print("Not found")
