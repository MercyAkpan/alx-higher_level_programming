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
    search = sys.argv[4]
    connection = f"mysql+mysqldb://{user}:password1@localhost:3306/{db}"
    engine = create_engine(connection)
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(State).filter(State.name.like((search))).all()
    if not res:
        print("Not found")
#   ABOVE. This  returns a list of the State objects
    else:
        print(f"{res[0].id}")
    # To access the list(res), use each row attribute, not index
    session.close()
