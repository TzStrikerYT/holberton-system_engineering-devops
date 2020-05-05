#!/usr/bin/python3
""" USING A REST API THAT RETURN INFORMATION """
import json
import requests
from sys import argv

if __name__ == "__main__":
    """ prints info about employee """

    all_u = requests.get("http://jsonplaceholder.typicode.com/users")
    tasks = requests.get("http://jsonplaceholder.typicode.com/todos")

    try:
        all_users = all_u.json()
        all_t = tasks.json()

    except ValueError:
        print("Not Valid JSON")

    master = {}
    usernames = {}

    for user in all_users:
        username = user.get("username")
        user_id = user.get("id")
        master[user_id] = []
        usernames[user_id] = username

    for task in all_t:
        user_id = task.get("userId")
        d_task = {
            "username": usernames.get(user_id),
            "task": task.get("title"),
            "completed": task.get("completed")
        }
        if master.get(user_id) is not None:
            master.get(user_id).append(d_task.copy())

    print(master)

    _file = "todo_all_employees.json"
    with open(_file, "w", newline="") as f:
        json.dump(master, f)
