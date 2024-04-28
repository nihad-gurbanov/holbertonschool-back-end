#!/usr/bin/python3


import json
import requests
import sys


"""
    Exports data in JSON format.
"""


def export_to_json(employee_id):
    """
    Exports the employee's TODO list to a JSON file.

    Args:
    - employee_id (int): The ID of the employee.
    """
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
        ).json()
    username = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        ).json().get('username')

    tasks_dict = {str(employee_id): []}

    for task in todos:
        task_data = {
            "task": task['title'],
            "completed": task['completed'],
            "username": username
        }
        tasks_dict[str(employee_id)].append(task_data)

    filename = f"{employee_id}.json"
    with open(filename, 'w') as json_file:
        json.dump(tasks_dict, json_file, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit()

    employee_id = int(sys.argv[1])
    export_to_json(employee_id)
