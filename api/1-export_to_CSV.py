#!/usr/bin/python3

""" Python script that gathers data from the JSON Placeholder API
for a given employee ID, and exports information about the user's TODO
list progress to a csv file.
"""


import csv
import requests
import sys


API_URL = "https://jsonplaceholder.typicode.com"


def export_todo_to_csv(employee_id):
    """Input: integer, employee_id.

    Returns: None, exports the employee TODO
    list progress to a csv file.
    """
    user = requests.get(f"{API_URL}/users/{employee_id}").json()
    todos = requests.get(f"{API_URL}/todos").json()
    employee_todos = [x for x in todos if x.get("userId") == employee_id]
    tasks_completed = [x for x in employee_todos if x.get("completed")]

    employee_name = user.get("name")

    headers = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    rows = [
        {
            "USER_ID": employee_id,
            "USERNAME": employee_name,
            "TASK_COMPLETED_STATUS": task.get("completed"),
            "TASK_TITLE": task.get("title"),
        }
        for task in employee_todos
    ]

    with open(f"{employee_id}.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writerows(rows)


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    export_todo_to_csv(employee_id)
