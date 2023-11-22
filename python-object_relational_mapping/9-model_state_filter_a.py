#!/usr/bin/python3
"""a script that lists all State objects that
contain the letter a from the database
hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # Create engine that connects to the core (MySQL)
    # The dialect is mysql, the driver is mysqldb
    # user:password@host:port/database
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Generates new Session objects when called
    Session = sessionmaker(bind=engine)

    # instance of Session class
    session = Session()

    # Querying data from the State table that contain
    # the letter a
    for State in session.query(State).filter(State.name.like('%a%').order_by(State.id)):
        print("{}: {}".format(State.id, State.name))

    # Close the session
    session.close()
