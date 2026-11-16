#!/usr/bin/python3
"""Exports all TODO tasks of all employees to a JSON file."""
import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    users = requests.get("{}/users".format(base_url)).json()
    todos = requests.get("{}/todos".format(base_url)).json()

    usernames = {user.get("id"): user.get("username") for user in users}
    data = {str(user.get("id")): [] for user in users}

    for task in todos:
        user_id = task.get("userId")
        data.setdefault(str(user_id), []).append({
            "username": usernames.get(user_id),
            "task": task.get("title"),
            "completed": task.get("completed")
        })

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(data, json_file)
