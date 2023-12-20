#!/usr/bin/python3


""" a Python script that, using this REST API,
for a given employee ID,
returns information about his/her
TODO list progress."""
import json
import requests
import sys


def todo_list(employee_ID):
    """
    Retrieve employee information and TODO
    list progress based on the employee ID.
    """
    url = 'https://jsonplaceholder.typicode.com/users'
    users_response = requests.get(url)
    users_data = users_response.json()

    if users_response.status_code == 200:
        all_employees_data = {}

        for user in users_data:
            employee_ID = user['id']
            employee_name = user['username']

            todos_url = f"{url}/{employee_ID}/todos"
            # getting todos url.
            todos_response = requests.get(todos_url)

            # converting into json format
            todos_data = todos_response.json()

            # verifying if request was a success
            if todos_response.status_code == 200:
                employee_tasks = []
                for task in todos_data:
                    employee_tasks.append({
                        "task": task['title'],
                        "completed": task['completed'],
                        "username": employee_name
                    })

                all_employees_data[str(employee_ID)] = employee_tasks

        # appending datas into the json file
        json_path = f"{employee_ID}.json"
        with open(json_path, 'w') as json_file:
            json.dump({str(employee_ID): employee_tasks}, json_file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("error")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    todo_list(employee_id)
