#!/usr/bin/python3

"""Python script that gathers data from the JSON Placeholder API,
and exports information about all users' TODO list progress to a
JSON file.
"""

import json
import requests


API_URL = "https://jsonplaceholder.typicode.com"


def export_all_todos_to_json():
    """Input: None.

    Returns: None, exports all employees' TODO list progress to a JSON file.
    """
    users = requests.get(f"{API_URL}/users").json()
    todos = requests.get(f"{API_URL}/todos").json()

    username_map = {user.get("id"): user.get("username") for user in users}

    all_tasks = {}
    for user_id, username in username_map.items():
        user_todos = [t for t in todos if t.get("userId") == user_id]
        all_tasks[str(user_id)] = [
            {
                "username": username,
                "task": t.get("title"),
                "completed": t.get("completed"),
            }
            for t in user_todos
        ]

    with open("todo_all_employees.json", "w", encoding="utf-8") as file:
        json.dump(all_tasks, file)


if __name__ == "__main__":
    export_all_todos_to_json()
