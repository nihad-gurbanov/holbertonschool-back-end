#!/usr/bin/python3

import requests
import sys


def get_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    todos_url = f"{base_url}/todos"
    user_url = f"{base_url}/users/{employee_id}"

    try:
        todos_response = requests.get(
            todos_url, params={"userId": employee_id})
        todos = todos_response.json()

        user_response = requests.get(user_url)
        user_data = user_response.json()
        username = user_data["name"]

        total = len(todos)
        completed = sum(1 for todo in todos if todo['completed'])

        print(f"Employee {username} is done with tasks ({completed}/{total}):")
        for todo in todos:
            if todo['completed']:
                print(f"\t{todo['title']}")

    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_todo_progress(employee_id)
