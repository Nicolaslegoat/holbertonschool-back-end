#!/usr/bin/python3


""" a Python script that, using this REST API,
for a given employee ID,
returns information about his/her
TODO list progress."""
import csv
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
    url = 'https://jsonplaceholder.typicode.com'

    # url for employess and todos
    employee_url = f"{url}/users/{employee_ID}"
    todos_url = f"{url}/todos?userId={employee_ID}"

    # request to get employee url
    employee_response = requests.get(employee_url)

    # converting to json format
    employee_data = employee_response.json()

    # verifying that request is a success
    if employee_response.status_code == 200:
        # get the employee's name
        employee_name = employee_data.get('username')

    # getting todos url.
    todos_response = requests.get(todos_url)

    # converting into json format
    todos_data = todos_response.json()

    # verifying if request was a success
    if todos_response.status_code == 200:
        # gettin total number of tasks in todos
        total_tasks = len(todos_data)
        # variable to be incremented if task is completed
        completed_tasks = 0

        csv_path = f"{employee_ID}.csv"
        with open(csv_path, 'w', newline='') as csvfile:
            fieldname = [
                'USER_ID',
                'USERNAME',
                "TASK_COMPLETED_STATUS",
                "TASK_TITLE"
                ]
        writer = csv.DictWriter(csvfile,
                                fieldname=fieldname,
                                quoting=csv.QUOTE_ALL)

        for task in todos_data:
            writer.writenow({
                "USER_ID": employee_ID,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": task['completed'],
                "TASK_TITLE": task['title']
            })


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("error")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    to_do(employee_id)
