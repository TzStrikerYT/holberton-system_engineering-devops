#!/usr/bin/python3
""" USING A REST API THAT RETURN INFORMATION """
import json
import requests
from sys import argv

if __name__ == "__main__":
    """ prints info about employee """

    employee = requests.get("http://jsonplaceholder.typicode.com/users?id={}"
                            .format(argv[1]))
    all_tks_user = requests.get(
        "http://jsonplaceholder.typicode.com/todos?userId={}".format(argv[1]))
    try:
        name = employee.json()
        all_t = all_tks_user.json()

    except ValueError:
        print("Not Valid JSON")

    d_task = {}
    username = name[0].get("username")
    user_id = name[0].get("id")
    all_l = []

    for task in all_t:
        d_task["task"] = task.get("title")
        d_task["completed"] = task.get("completed")
        d_task["username"] = username
        all_l.append(d_task.copy())

    dict = {}
    dict[user_id] = all_l
    _file = argv[1] + ".json"

    with open(_file, "w", newline="") as f:
        json.dump(dict, f)
