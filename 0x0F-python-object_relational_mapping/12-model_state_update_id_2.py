#!/usr/bin/python3
'''
script that changes the name of a State object from the
database hbtn_0e_6_usa
'''

import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":

    if len(sys.argv) != 4:
        sys.exit(1)

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    with Session() as session:
        change_name = session.query(State).filter_by(id=2).one()
        change_name.name = 'New Mexico'
        session.commit()
