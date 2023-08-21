#!/usr/bin/python3
"""This script lists all State objects from the database hbtn_0e_6_usa"""
from model_state import Base, State
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    eng_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            argv[1], argv[2], argv[3]
            )
    engine = create_engine(eng_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()
