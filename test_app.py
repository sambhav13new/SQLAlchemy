import unittest
import json
from unittest.mock import patch
from app import app


class AppTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_add_employee_endpoint(self):
        employee_data = {"name": "John Doe", "age": 30, "position": "Software Engineer"}

        with patch('worker.process_employee_data') as mock_process_employee_data:
            response = self.app.post('/add_employee', json=employee_data)

            mock_process_employee_data.assert_called_with(employee_data)
            self.assertEqual(response.status_code, 200)
            self.assertEqual(json.loads(response.get_data()), {'message': 'Employee data added successfully'})


if __name__ == '__main__':
    unittest.main()