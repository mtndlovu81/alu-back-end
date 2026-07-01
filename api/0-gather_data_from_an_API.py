#!/usr/bin/python3

""" Python script that gathers data from the JSON Placeholder API
for a given employee ID, returns information about the user's TODO
list progress.
"""


import requests
import sys


API_URL = "https://jsonplaceholder.typicode.com"


def display_todo(employee_id):
    """Input: integer, employee_id.

    Returns: None, displays the employee TODO
    list progress to standard output.
    """
    user = requests.get(f"{API_URL}/users/{employee_id}").json()
    todos = requests.get(f"{API_URL}/todos").json()
    employee_todos = [x for x in todos if x.get("userId") == employee_id]
    tasks_completed = [x for x in employee_todos if x.get("completed")]

    employee_name = user.get("name")
    total_tasks = len(employee_todos)
    tasks_done = len(tasks_completed)

    print(f"Employee {employee_name} is done with tasks"
          f"({tasks_done}/{total_tasks}):")

    for task in tasks_completed:
        print(f"\t {task.get('title')}")


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    display_todo(employee_id)
