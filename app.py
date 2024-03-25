from flask import Flask, request, jsonify
from worker import process_employee_data

app = Flask(__name__)

# Flask POST endpoint to add employee data
@app.route('/add_employee', methods=['POST'])
def add_employee():
    try:
        # Get employee data from the POST request
        employee_data = request.get_json()

        # Process employee data concurrently using threads
        process_employee_data(employee_data)

        return jsonify({'message': 'Employee data added successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
