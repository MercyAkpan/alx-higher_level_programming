#!/usr/bin/python3
""" SQLALCHEMY MODULE """
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


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


engine = create_engine("""mysql+mysqldb://meme
                       :password1@localhost:3306/
                       hbtn_0e_6_usa""", echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
