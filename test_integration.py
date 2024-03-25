import pytest
import requests
import time

# Define the base URL of the Flask application running in Docker
BASE_URL = "http://127.0.0.1:5000"

# Define the path to the Docker Compose file
DOCKER_COMPOSE_FILE = "docker-compose.yml"

# Set up the Docker Compose fixture
@pytest.fixture(scope="session")
def docker_compose_file(pytestconfig):
    return str(pytestconfig.rootpath.joinpath(DOCKER_COMPOSE_FILE))

# Set up the Docker service fixture
@pytest.fixture(scope="session")
def flask_app(docker_services, docker_compose_file):
    # Wait for the Flask app to be ready
    docker_services.wait_for_service("flask", 5000)
    return BASE_URL

# Integration test to check if the Flask app is running
def test_flask_app_running(flask_app):
    response = requests.get(f"{flask_app}/add_employee")
    assert response.status_code == 200

# Integration test to check if adding an employee works
def test_add_employee(flask_app):
    employee_data = {"name": "John Doe", "age": 30, "position": "Software Engineer"}
    response = requests.post(f"{flask_app}/add_employee", json=employee_data)
    assert response.status_code == 200
    assert response.json() == {'message': 'Employee data added successfully'}

if __name__ == "__main__":
    pytest.main([__file__])
