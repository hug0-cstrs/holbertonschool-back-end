#!/usr/bin/python3
"""
Python script that for a given employee ID returns all his todo list
and exports the data in CSV format
"""

import csv
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

    csv_f = '{}.csv'.format(sys.argv[1])
    with open(csv_f, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in json_todo:
            csv_writer.writerow([json_names['id'], json_names['username'],
                                 task["completed"], task["title"]])