#!/usr/bin/python3

"""
    Exports the employee's TODO list to a CSV file.

"""

import csv
import requests
from sys import argv


def add_to_csv():
    """
        This function adds data to CSV file
    """
    if len(argv) < 2:
        exit()

    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos?userId={argv[1]}"
        ).json()
    username = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
        ).json().get('username')

    row = ''
    for task in todos:
        title = task['title']
        status = task['completed']
        row += f'"{argv[1]}","{username}","{status}","{title}"\n'

    filename = argv[1] + '.csv'

    "Open and write csv file"
    with open(filename, 'w') as csvfile:
        csvfile.write(row)


if __name__ == "__main__":
    add_to_csv()
