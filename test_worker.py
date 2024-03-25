import unittest
from unittest.mock import patch
from worker import process_employee_data, write_to_database, Employee, db_session, engine

class WorkerTestCase(unittest.TestCase):

    def setUp(self):
        # Create tables
        Employee.metadata.create_all(bind=engine)

    def tearDown(self):
        # Drop tables after tests
        Employee.metadata.drop_all(bind=engine)

    @patch('worker.ThreadPoolExecutor')
    def test_process_employee_data(self, mock_thread_pool_executor):
        employee_data = {"name": "John Doe", "age": 30, "position": "Software Engineer"}

        # Mock thread pool executor to avoid actual thread execution in tests
        mock_executor_instance = mock_thread_pool_executor.return_value
        with patch.object(mock_executor_instance, 'submit') as mock_submit:
            process_employee_data(employee_data)

            # Verify that write_to_database was called with the correct arguments
            mock_submit.assert_called_with(write_to_database, employee_data)

if __name__ == '__main__':
    unittest.main()
