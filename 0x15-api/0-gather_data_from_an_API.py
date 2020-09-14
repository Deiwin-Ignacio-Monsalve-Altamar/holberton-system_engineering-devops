#!/usr/bin/python3
"""using this REST API, for a given employee ID"""
import requests
import sys


def gatherDataFromaAPI(id_users):
    """Gather data from an API"""
    url_todo = "https://jsonplaceholder.typicode.com/todos"
    url_users = "https://jsonplaceholder.typicode.com/users/{}".format(
        id_users)

    users_employ = requests.get(url_users)
    todo_employ = requests.get(url_todo)

    employ_name = users_employ.json().get('name')
    tasks_num, comp_tasks = 0, []

    for tasks in todo_employ.json():
        if tasks.get('userId') == int(id_users):
            tasks_num += 1
            if tasks.get('completed') is True:
                comp_tasks.append(tasks)

    print('Employee {} is \done with tasks({}/{}):'
          .format(employ_name, len(comp_tasks), tasks_num))
    for task in comp_tasks:
        print('\t {}'.format(task.get('title')))


if __name__ == '__main__':
    if len(sys.argv) == 2:
        gatherDataFromaAPI(sys.argv[1])
