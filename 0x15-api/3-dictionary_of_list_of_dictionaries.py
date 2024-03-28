#!/usr/bin/python3
"""This script is used to gather info from an API"""

import json
import requests
import sys


def get_employee_details():
    """This function gets the emplyee details"""
    user_url = "https://jsonplaceholder.typicode.com/users"
    todo_url = "https://jsonplaceholder.typicode.com/todos"

    user_res = requests.get(user_url)
    todo_res = requests.get(todo_url)

    if user_res.status_code != 200 or todo_res.status_code != 200:
        print("Error: Unable to fetch data from API")
        return
    user_data = user_res.json()
    todo_data = todo_res.json()

    dic = {}
    for user in user_data:
        task_list = []
        for task in todo_data:
            if task.get('userId') == user.get('id'):
                task_list.append({
                    "username": user.get("username"),
                    "task": task.get("title"),
                    "completed": task.get("completed")
                })
        dic[f'{user.get("id")}'] = task_list

    with open("todo_all_employees.json", 'w') as f:
        json.dump(dic, f)
# print(f"Employee {user_data.get('name')} is done with tasks({nodt}/{nt}):")
#    for task in todo_data:
#        if task.get('completed'):
#            print("\t " + task.get('title'))


if __name__ == "__main__":
    get_employee_details()
