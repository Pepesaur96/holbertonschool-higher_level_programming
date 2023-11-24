#!/usr/bin/python3
"""a script that creates the State “California”
with the City “San Francisco” from the database
hbtn_0e_100_usa: (100-relationship_states_cities.py)"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
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

    # Create a new state California and a new city San Francisco
    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)
    new_state.cities.append(new_city)

    # Add the new state and city to the database
    session.add(new_state)
    session.add(new_city)

    # Commit the record to the database
    session.commit()

    # Close the session
    session.close()
