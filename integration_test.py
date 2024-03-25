import pytest
import requests
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import app

# Define the Docker Compose configuration for the test environment
@pytest.fixture(scope='session')
def docker_compose_file(pytestconfig):
    return str(pytestconfig.rootpath / 'docker-compose-test.yml')

# Set up the SQLAlchemy test database
@pytest.fixture(scope='session')
def db_engine(docker_services):
    database_url = f"postgresql://user:password@{docker_services.host()}:5432/testdatabase"
    engine = create_engine(database_url)

    # Wait until the database is ready
    docker_services.wait_until_responsive(
        timeout=30.0, pause=0.1,
        check=lambda: engine.execute("SELECT 1").fetchone() is not None
    )

    return engine

# Set up the Flask application with the test database
@pytest.fixture
def app_with_test_db(db_engine):
    app.config['SQLALCHEMY_DATABASE_URI'] = db_engine.url
    app.testing = True

    # Apply any other necessary configurations

    with app.app_context():
        yield app

# Set up a test session and Flask client
@pytest.fixture
def test_client(app_with_test_db):
    with app_with_test_db.test_client() as client:
        yield client

# Integration test for the Flask application
def test_add_employee_endpoint(test_client):
    employee_data = {"name": "John Doe", "age": 30, "position": "Software Engineer"}

    # Make a POST request to the /add_employee endpoint
    response = test_client.post('/add_employee', json=employee_data)

    assert response.status_code == 200
    assert json.loads(response.get_data()) == {'message': 'Employee data added successfully'}
