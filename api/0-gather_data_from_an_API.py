#!/usr/bin/python3
"""Returns TODO list progress for a given employee ID using a REST API."""
import requests
import sys


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"
    user_id = int(sys.argv[1])

    user = requests.get("{}/users/{}".format(base_url, user_id)).json()
    todos = requests.get("{}/todos".format(base_url),
                         params={"userId": user_id}).json()

    done = [task for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todos)))
    for task in done:
        print("\t {}".format(task.get("title")))
