#!/usr/bin/python3
"""prrints all City objects from the
database hbtn_0e_14_usa"""

from sys import argv
from model_state import Base, State
from model_city import Base, City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

    # Create engine that connects to the core
    # (MySQL) The dialect is mysql, the driver
    # is mysqldb user:password@host:port/database
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}"
        .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

    # Generates new Session objects when called
    Session = sessionmaker(bind=engine)

    # instance of Session class
    session = Session()

    # Querying data from the states table
    for city, state in session.query(City, State).\
            filter(City.state_id == State.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    # Close the session
    session.close()
