#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the CSV format.
"""
import csv
from requests import get
from sys import argv

if __name__ == '__main__':
    userId = argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    user_url = '{}/users/{}'.format(url, userId)
    todo_url = '{}/todos?userId={}'.format(url, userId)
    user = get(user_url).json()
    todo = get(todo_url).json()
    name = user.get('username')

    filename = userId + '.csv'
    with open(filename, 'w', newline='') as csvfile:
        taskWriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            taskWriter.writerow([int(userId), name, task.get('completed'), 
                task.get('title')])
