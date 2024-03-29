#!/usr/bin/python3
'''returns the information about the TODO list progress by the employee id.'''
import requests
from sys import argv


if __name__ == '__main__':
    data = requests.get('https://jsonplaceholder.typicode.com/todos')
    data = data.json()
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    users = users.json()
    user = [i for i in users if i.get('id') == int(argv[1])][0]
    tasks = [i for i in data if i.get('userId') == int(argv[1])]
    completed = [i for i in tasks if i.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get('name'), len(completed), len(tasks)))
    for task in completed:
        print("\t {}".format(task.get('title')))
