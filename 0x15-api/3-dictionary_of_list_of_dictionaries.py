#!/usr/bin/python3
"""
export all data in json format
"""
import json
from requests import get

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    user_url = '{}users'.format(url)
    todo_url = '{}todos'.format(url)
    users = get(user_url).json()
    todo = get(todo_url).json()
    mainDict = {}

    for user in users:
        userList = []
        username = user.get("username")
        userId = user.get("id")
        for task in todo:
            if task.get("userId") == userId:
                userList.append({"username": username,
                            "task": task.get("title"),
                            "completed": task.get("completed")})
        mainDict[userId] = userList
    
    with open('todo_all_employees.json', 'w') as filejson:
        json.dump(mainDict, filejson)
