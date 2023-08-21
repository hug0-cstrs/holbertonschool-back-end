#!/usr/bin/python3
"""
Python script that for a given employee ID returns all his todo list
and exports the data in json format
"""
import requests
import sys
import json

if __name__ == "__main__":
    to_do = requests.get('https://jsonplaceholder.typicode.com/todos?userId=' +
                         sys.argv[1], timeout=5)
    names = requests.get('https://jsonplaceholder.typicode.com/users/' +
                         sys.argv[1], timeout=5)

    json_todo = to_do.json()
    json_names = names.json()

    all_tasks = 0
    tasks_completed = 0

    titles_completed = []
    for task in json_todo:
        all_tasks += 1
        if task["completed"] is True:
            tasks_completed += 1
            titles_completed.append(task["title"])

    tasks_data = []

    for task in json_todo:
        task_data = {
            "task": task["title"],
            "completed": task["completed"],
            "username": json_names["name"]
        }
        tasks_data.append(task_data)

    employee_data = {
        sys.argv[1]: tasks_data
    }

    json_data = json.dumps(employee_data)

    json_f = '{}.json'.format(sys.argv[1])

    with open(json_f, "w") as file:
        file.write(json_data)
