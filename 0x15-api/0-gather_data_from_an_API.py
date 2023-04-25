#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) > 1:
        userId = argv[1]
        url = 'https://jsonplaceholder.typicode.com/'
        r = requests.get('{}users/{}'.format(url, userId))
        name = r.json().get('name')

        todos = requests.get('{}todos?userId={}'
                             .format(url, userId)).json()
        totalTask = len(todos)
        completedTask = []
        for task in todos:
            if task.get('completed') is True:
                completedTask.append(task)
        count = len(completedTask)

        print('Emloyee {} is done with tasks({}/{}'
              .format(name, count, totalTask))

        for title in completedTask:
            print("\t {}".format(title.get("title")))
