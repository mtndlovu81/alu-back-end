#!/usr/bin/python3

"""Python script that gathers data from the JSON Placeholder API
for a given employee ID, and exports information about the user's TODO
list progress to a JSON file.
"""

import json
import requests
import sys


API_URL = "https://jsonplaceholder.typicode.com"


def export_todo_to_json(employee_id):
    """Input: integer, employee_id.

    Returns: None, exports the employee TODO
    list progress to a JSON file.
    """
    user = requests.get(f"{API_URL}/users/{employee_id}").json()
    todos = requests.get(f"{API_URL}/todos").json()
    employee_todos = [x for x in todos if x.get("userId") == employee_id]
    employee_name = user.get("username")

    tasks = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": employee_name,
        }
        for task in employee_todos
    ]

    with open(f"{employee_id}.json", "w", encoding="utf-8") as file:
        json.dump({str(employee_id): tasks}, file)


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    export_todo_to_json(employee_id)
