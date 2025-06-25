#!/usr/bin/python3
"""
Script that creates the State “California” with the City
“San Francisco” in the database hbtn_0e_100_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql username> <mysql password> <database name>"
              .format(sys.argv[0]))
        sys.exit(1)

    # Create engine and bind to MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    # Create all tables
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Create new State and City objects
    california = State(name="California")
    san_francisco = City(name="San Francisco")

    # Establish relationship
    california.cities.append(san_francisco)

    # Add to session and commit
    session.add(california)
    session.add(san_francisco)
    session.commit()

    # Close session
    session.close()
