#!/usr/bin/python3
"""
Python script that retrieves all tasks from all employees and
exports the data in JSON format.
"""

import json
import requests
import sys


if __name__ == "__main__":
    # requête HTTP GET pour récupérer les noms des employés
    names = requests.get('https://jsonplaceholder.typicode.com/users')

    # convertit la réponse JSON en un objet Python
    json_names = names.json()

    # Création d'un dictionnaire vide pour stocker les tâches de chaque employé
    general_dict = {}

    # Parcours de chaque employé dans la liste des noms
    for user in json_names:

        # Création d'une liste vide pour stocker les tâches de cet employé
        this_list = []

        # requête HTTP GET pour récupérer les tâches de l'employé
        to_do = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId=' +
            str(user['id']))

        # Conversion de la réponse JSON en un objet Python
        json_todo = to_do.json()

        # Parcours de chaque tâche dans la liste des tâches de l'employé
        for item in json_todo:

            # Création d'un dictionnaire pour stocker les détails de la tâche
            task_dict = {}
            task_dict["task"] = item['title']
            task_dict["completed"] = item['completed']
            task_dict["username"] = user['username']
            this_list.append(task_dict)

        # Ajout de ce dictionnaire à la liste des tâches de l'employé
        general_dict[user['id']] = this_list

    # Définition du nom du fichier JSON
    json_f = 'todo_all_employees.json'

    # Écriture du dictionnaire général dans le fichier JSON
    with open(json_f, mode='w') as json_file:
        json.dump(general_dict, json_file)
