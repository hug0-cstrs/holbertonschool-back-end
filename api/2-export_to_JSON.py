#!/usr/bin/python3
"""
Python script that for a given employee ID returns all his todo list
and exports the data in json format
"""
import json
import requests
import sys


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

    my_dict = {}
    this_list = []

    for item in json_todo:
        task_dict = {}
        task_dict["task"] = item['title']
        task_dict["completed"] = item['completed']
        task_dict["username"] = json_names['username']
        this_list.append(task_dict)

    my_dict[sys.argv[1]] = this_list

    json_f = sys.argv[1] + '.json'
    with open(json_f, mode='w') as json_file:
        json.dump(my_dict, json_file)
