#!/usr/bin/python3
'''
script that prints the first State object from the database hbtn_0e_6_usa
'''

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import sessionmaker
    from sqlalchemy import create_engine

    if len(sys.argv) != 4:
        sys.exit(1)

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()

    query_first = session.query(State).order_by(State.id).first()

    if query_first is None:
        print(f"Nothing")
    else:
        print(f"{query_first.id}: {query_first.name}")

    session.close()
