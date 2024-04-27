#!/usr/bin/python3

"""
    This script retrieves and displays information about a user's
    completed tasks from the JSONPlaceholder API.
    Usage: python3 script_name.py user_id
"""
if __name__ == "__main__":
    import requests
    from sys import argv

    if len(argv) < 2:
        exit()

    todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
        )
    data = todo.json()
    user_data = user.json()

    completed = 0
    completed_task_list = []
    total = 0

    username = user_data["name"]
    for todo in data:
        if todo["userId"] == int(argv[1]):
            total += 1
        if todo["userId"] == int(argv[1]) and todo['completed']:
            completed += 1
            completed_task_list.append('\t' + todo['title'])

    print(
        f"Employee {username} is done with tasks({completed}/{total}):"
        )
    for i in completed_task_list:
        print(i)
