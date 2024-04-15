#!/usr/bin/python3
""" SQLALCHEMY MODULE for connecting to the Datbase
"""
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import sys

Base = declarative_base()
# user = sys.argv[1]
# pswd = sys.argv[2]
# db = sys.argv[3]
# connection = f"mysql+mysqldb://{user}:{pswd}@localhost:3306/{db}"
# engine = create_engine(connection)
# Base.metadata.create_all(bind=engine)
# Session = sessionmaker(bind=engine)
# session = Session()


class State(Base):
    """ THIS IS A CLASS MAPPED TO A TABLE
    """
    __tablename__ = "states"
    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(128))

#    def __init__(self, name):
#        """ THIS IS THE INIT FUNCTION
#        """
#        self.name = name
