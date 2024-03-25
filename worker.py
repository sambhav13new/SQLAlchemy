from concurrent.futures import ThreadPoolExecutor
from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

# SQLAlchemy configuration
DATABASE_URL = "postgresql://user:password@localhost:5433/mydatabase"
engine = create_engine(DATABASE_URL, echo=True)
Base = declarative_base()

# Declarative model definition
class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, Sequence('employee_id_seq'), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    position = Column(String(50))

Base.metadata.create_all(engine)

# Create a thread-local scoped session
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Function to perform database writes
def write_to_database(employee_data):
    session = db_session()
    new_employee = Employee(**employee_data)
    session.add(new_employee)
    session.commit()

# Function to be executed by threads
def process_employee_data(employee_data):
    with ThreadPoolExecutor() as executor:
        # Submit multiple write tasks to the thread pool
        for _ in range(5):
            executor.submit(write_to_database, employee_data)
