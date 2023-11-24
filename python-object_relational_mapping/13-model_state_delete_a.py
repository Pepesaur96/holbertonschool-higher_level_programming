#!/usr/bin/python3
"""a script that deletes all State
objects with a name containing the letter
a from the database hbtn_0e_6_usa"""

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

    # Generates new Session objects when called
    Session = sessionmaker(bind=engine)

    # instance of Session class
    session = Session()

    # Querying data from the states table
    query = session.query(State).filter(State.name.contains('a')).all()

    # Delete all the rows
    for row in query:
        session.delete(row)

    # Commit the changes
    session.commit()

    # Close the session
    session.close()
