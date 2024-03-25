import json
import pytest
from app import app
from worker import process_employee_data
from pytest_benchmark.fixture import BenchmarkFixture


@pytest.fixture
def flask_app():
    return app.test_client()


@pytest.fixture
def employee_data():
    return {"name": "John Doe", "age": 30, "position": "Software Engineer"}


# Benchmark the time taken to add an employee to the database
def test_add_employee_benchmark(benchmark: BenchmarkFixture, flask_app, employee_data):
    # Wrap the benchmarked function in a lambda to pass arguments
    result = benchmark(lambda: flask_app.post('/add_employee', json=employee_data))

    # Assert the response status code and message
    assert result.status_code == 200
    assert json.loads(result.get_data()) == {'message': 'Employee data added successfully'}
