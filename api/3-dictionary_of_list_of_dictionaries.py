#!/usr/bin/python3
"""
Python script that retrieves all tasks from all employees and
exports the data in JSON format.
"""

import json
import requests
import sys


if __name__ == "__main__":
    all_tasks = {}
    # Get all employees
    for user_id in range(1, 11):
        to_do = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId='
            + str(user_id), timeout=5)
        names = requests.get(
            'https://jsonplaceholder.typicode.com/users/'
            + str(user_id), timeout=5)

        # Convert to JSON
        json_todo = to_do.json()
        json_names = names.json()

        # Count completed tasks
        tasks_completed = 0
        titles_completed = []

        # Task data construction
        for task in json_todo:
            if task["completed"]:
                tasks_completed += 1
                titles_completed.append(task["title"])

        # Employee data construction
        employee_data = {
            "username": json_names['username'],
            "tasks": [{"task": title, "completed": True}
                      for title in titles_completed]
        }

        # Employee data storage
        all_tasks[str(user_id)] = employee_data

    # Export JSON
    json_data = json.dumps(all_tasks)

    # Write to file
    with open('todo_all_employees.json', mode='w') as json_file:
        json_file.write(json_data)
