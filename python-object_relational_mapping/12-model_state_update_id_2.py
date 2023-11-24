#!/usr/bin/python3
"""a script that changes the name of a
State object from the database hbtn_0e_6_usa"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # Create engine that connects to the core
    # (MySQL) The dialect is mysql, the driver
    # is mysqldb user:password@host:port/database
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Create all the objects in the database
    Base.metadata.create_all(engine)

    # Generates new Session objects when called
    Session = sessionmaker(bind=engine)

    # instance of Session class
    session = Session()

    # Querying data from the states table
    query = session.query(State).filter(State.id == 2).first()
    query.name = "New Mexico"
    session.commit()

    # Close the session
    session.close()
