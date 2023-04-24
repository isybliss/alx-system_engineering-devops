#!/usr/bin/python3
"""
export data in the JSON format
"""
import json
from requests import get
from sys import argv

if __name__ == '__main__':
    userId = argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    user_url = '{}/users/{}'.format(url, userId)
    user = get(user_url).json()
    todo_url = '{}/todos?userId={}'.format(url, userId)
    todo = get(todo_url).json()
    name = user.get('username')

    userTodo = {}
    taskList = []

    for task in todo:
        taskDict = {"task": task.get('title'),
                    "completed": task.get('completed'),
                    "username": name}
        taskList.append(taskDict)
    userTodo[userId] = taskList

    filename = userId + '.json'
    with open(filename, 'w') as fjs:
        json.dump(userTodo, fjs)
