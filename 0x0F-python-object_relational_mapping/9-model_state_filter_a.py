#!/usr/bin/python3
""" SQLALCHEMY MODULE for connecting to the Datbase
"""
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from model_state import Base, State
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

    res = session.query(State).filter(State.name.like(('%a%'))).all()
#    ABOVE. This  returns a list of the State objects
    for data in res:
        print(f"{data.id}: {data.name}")
    # To access the list(res), use each row attribute, not index
    session.close()
