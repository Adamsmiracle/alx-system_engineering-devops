#!/usr/bin/python3
"""This script is used to gather info from an jsonplaceholder
API
"""

import requests
import sys


def get_employee_details(e_id):
    """This function gets the employee details"""
    user_url = f"https://jsonplaceholder.typicode.com/users/{e_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/user/{e_id}/todos"

    user_res = requests.get(user_url)
    todo_res = requests.get(todo_url)

    if user_res.status_code != 200 or todo_res.status_code != 200:
        print("Error: Unable to fetch data from API")
        return
    user_data = user_res.json()
    todo_data = todo_res.json()

    nt = len(todo_data)
    nodt = len([i for i in todo_data if i.get('completed')])

    with open(f"{e_id}.csv", "w") as f:
        for task in todo_data:
            f.write(f'"{e_id}","{user_data.get("username")}"'
                    f',"{task.get("completed")}","{task.get("title")}"\n')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <employee_id>")
        sys.exit(1)
    get_employee_details(sys.argv[1])
