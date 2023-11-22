#!/usr/bin/python3
"""a script that lists all State objects from the database hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # Create engine that connects to the core (MySQL)
    # The Engine, when first returned by create_engine(), has not actually
    # tried to connect to the database yet; that happens only the first time
    # it is asked to perform a task against the database.
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Generate database schema
    # The Table objects are then collected into MetaData instance.
    # The MetaData instance is a registry which includes the ability to emit
    # a limited set of schema generation commands to the database.
    Base.metadata.create_all(engine)

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # create a Session
    session = Session()

    # Querying is performed using the Query object.
    # The Query object is generative, meaning that most method calls return a
    # new Query object upon which further criteria may be added.
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
