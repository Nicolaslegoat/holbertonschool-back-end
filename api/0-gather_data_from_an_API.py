#!/usr/bin/python3
"""
Script that fetches and displays TODO list progress
for a given employee ID using a REST API.
"""

import requests
import sys


def todo_list(employee_id):
    """Fetch and display TODO list progress for a given employee."""

    base_url = 'https://jsonplaceholder.typicode.com'

    # URLs for employees and todos
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    # Request to get employee data
    employee_response = requests.get(employee_url)

    # Verify that the request was successful
    if employee_response.status_code != 200:
        print(f"Error fetching employee data. Status Code: {employee_response.status_code}")
        sys.exit(1)

    # Convert employee data to JSON format
    employee_data = employee_response.json()

    # Get employee name
    employee_name = employee_data.get('name')

    # Request to get TODOs data
    todos_response = requests.get(todos_url)

    # Verify that the request was successful
    if todos_response.status_code != 200:
        print(f"Error fetching TODOs data. Status Code: {todos_response.status_code}")
        sys.exit(1)

    # Convert TODOs data to JSON format
    todos_data = todos_response.json()

    # Calculate total tasks and completed tasks
    total_tasks = len(todos_data)
    completed_tasks = sum(task['completed'] for task in todos_data)

    # Print the progress of the employee's TODO list
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")

    # Print the titles of completed tasks
    for task in todos_data:
        if task['completed']:
            print(f"\t{task['title']}")


# Execute the script if it is the main entry point.
if __name__ == "__main__":

    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    # Convert the command-line argument to an integer
    employee_id = int(sys.argv[1])

    # Call the todo_list function
    todo_list(employee_id)
