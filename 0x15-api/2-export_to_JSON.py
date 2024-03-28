#!/usr/bin/python3
"""This script is used to gather info from an jsonplaceholder
API
"""

import json
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

    task_list = []
    for task in todo_data:
        task_list.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user_data.get('username')
        })
    with open(f'{e_id}.json', 'w') as f:
        json.dump({f"{e_id}": task_list}, f)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <employee_id>")
        sys.exit(1)
    get_employee_details(sys.argv[1])
