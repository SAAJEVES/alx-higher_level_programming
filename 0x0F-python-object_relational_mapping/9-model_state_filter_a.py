#!/usr/bin/python3
'''
script that lists all State objects that contain the letter
a from the database hbtn_0e_6_usa
'''

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    if len(sys.argv) != 4:
        sys.exit(2)

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    Base.metadat.create_all(engine)
    session = Session()

    query_a = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id).all()

    for row_a in query_a:
        print(f"{row_a.id}: {row_a.name}")
