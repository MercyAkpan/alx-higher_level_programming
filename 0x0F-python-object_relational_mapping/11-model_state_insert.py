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
    new_state = State(name="Louisiana")
    # Add the new state object to the session
    session.add(new_state)
    # Commit the session to save the state object to the database
    session.commit()
    # Print the id of the new state object
    print(new_state.id)
    session.close()
