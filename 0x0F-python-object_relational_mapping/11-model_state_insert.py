#!/usr/bin/python3
'''
script that adds the State object “Louisiana” to the
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
        new_row = State(name='Louisiana')
        session.add(new_row)
        newly_added = session.query(State).filter_by(name="Louisiana").one()
        print(newly_added.id)
        session.commit()
