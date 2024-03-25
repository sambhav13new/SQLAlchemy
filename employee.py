from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLAlchemy configuration
DATABASE_URL = "postgresql://user:password@localhost:5433/mydatabase"
engine = create_engine(DATABASE_URL, echo=True)

# Declarative base class for ORM
Base = declarative_base()

# Employee model definition
class Employee(Base):
    __tablename__ = 'employees'
    id = Column(Integer, Sequence('employee_id_seq'), primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    position = Column(String(50))

# Create tables
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Inserting a new employee
new_employee = Employee(name='John Doe', age=30, position='Software Engineer')
session.add(new_employee)
session.commit()

# Querying all employees
employees = session.query(Employee).all()
for employee in employees:
    print(f"Employee ID: {employee.id}, Name: {employee.name}, Age: {employee.age}, Position: {employee.position}")
