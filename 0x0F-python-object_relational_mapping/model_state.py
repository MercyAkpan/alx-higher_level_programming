#!/usr/bin/python3
""" SQLALCHEMY MODULE """
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
db = "hbtn_0e_6_usa"                                                       user = "meme"                                                              connection = f"mysql+mysqldb://{user}:password1@localhost:3306/{db}"       engine = create_engine(connection, echo=True)                              Base.metadata.create_all(bind=engine)                                      Session = sessionmaker(bind=engine)                                        session = Session()

class State(Base):
    """ THIS IS A CLASS MAPPED TO A TABLE
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        """ THIS IS THE INIT FUNCTION
        """
        self.name = name

