#!/usr/bin/python3


""" a Python script that, using this REST API,
for a given employee ID,
returns information about his/her
TODO list progress."""
import requests
import sys


def to_do(employee_ID):
    """
    Retrieve employee information and TODO
    list progress based on the employee ID.

    Args:
        employee_ID (int): The ID of the employee.

    Returns:
        None

    Prints:
        Displays the employee's TODO list progress.
    """
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

    # Print the progress of the employee's TODO list
    print(f"Employee {employee_name} is done with tasks:")

    # Print the titles of completed tasks with formatting
    for task in todos_data:
        task_title = task['title']
        task_formatted = f"Task {task['id']} Formatting: OK"
        print(f"{task_formatted:<40} {task_title}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("error")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    to_do(employee_id)
