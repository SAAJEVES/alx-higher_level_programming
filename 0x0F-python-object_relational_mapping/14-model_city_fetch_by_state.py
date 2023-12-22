#!/usr/bin/python3
'''
a script 14-model_city_fetch_by_state.py that prints all City
objects from the database hbtn_0e_14_usa
'''

if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine

    if len(sys.argv) != 4:
        sys.exit(1)

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    with Session() as session:
        query_res = session.query(State.name, City.id, City.name)
                .join(City, State.id == City.state_id)

        for val in query_res:
            print(f"{val[0]}: {val[1]} {val[2]}")
