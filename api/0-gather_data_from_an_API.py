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

    todo = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={argv[1]}"
        ).json()

    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
        ).json().get('name')

    completed = 0
    titles = ""
    total = len(todo)

    for item in todo:
        if item['completed']:
            completed += 1
            titles += '\t ' + item.get('title') + "\n"

    print(
        "Employee {} is done with tasks({}/{}):".format(user, completed, total)
        )
    if titles:
        print(titles[:-1])
