#!/usr/bin/python3
""" SQLALCHEMY MODULE """
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from model_state import Base, State
from model_city import City
import sys
if __name__ == "__main__":
    Base = declarative_base()
    user = sys.argv[1]
    pswd = sys.argv[2]
    db = sys.argv[3]
    connection = f"mysql+mysqldb://{user}:password1@localhost:3306/{db}"
    engine = create_engine(connection)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(City).join(State, City.state_id == State.id)
# ABOVE. This  returns a list of the State objects
    for city, state in query:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
