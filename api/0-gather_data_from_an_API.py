#!/usr/bin/python3

"""
This script retrieves and displays information about a user's
completed tasks from the JSONPlaceholder API.
Usage: python3 script_name.py user_id
"""

import requests
from sys import argv

if len(argv) < 2:
    print("Usage: python3 script_name.py user_id")
    exit(1)

todo = requests.get("https://jsonplaceholder.typicode.com/todos")
user = requests.get(f"https://jsonplaceholder.typicode.com/users/{argv[1]}")
data = todo.json()
user_data = user.json()

completed_task = 0
completed_task_list = []
total_tasks = 0

username = user_data["name"]
for todo in data:
    if todo["userId"] == int(argv[1]):
        total_tasks += 1
    if todo["userId"] == int(argv[1]) and todo['completed']:
        completed_task += 1
        completed_task_list.append('\t' + todo['title'])

print(
    f"Employee {username} is done with tasks({completed_task}/{total_tasks}):"
    )
for i in completed_task_list:
    print(i)
