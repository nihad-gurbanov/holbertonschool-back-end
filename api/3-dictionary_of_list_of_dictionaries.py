#!/usr/bin/python3

"""
    Exports data in JSON format.
"""

import json
import requests


def export_all_to_json():
    """
    Exports all employees' TODO lists to a single JSON file.
    """
    all_todos = {}

    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    for user in users:
        user_id = user['id']
        username = user['username']

        todos = requests.get(
            f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"
            ).json()

        user_tasks = []
        for task in todos:
            task_data = {
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            }
            user_tasks.append(task_data)

        all_todos[str(user_id)] = user_tasks

    filename = "todo_all_employees.json"
    with open(filename, 'w') as json_file:
        json.dump(all_todos, json_file, indent=4)


if __name__ == "__main__":
    export_all_to_json()
