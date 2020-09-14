#!/usr/bin/python3
"""using this REST API, for a given employee ID"""
import requests
import sys


def get_todo(users_id):
    '''prints employees with completed to_do list'''

    to_do_url = 'http://jsonplaceholder.typicode.com/todos'
    employee_url = 'http://jsonplaceholder.typicode.com/users/{}'.format(
        users_id)
    e = requests.get(employee_url)
    to_do = requests.get(to_do_url)

    employee_name = e.json().get('name')
    n_task, comp_tasks = 0, []
    for task in to_do.json():
        if task.get('userId') == int(users_id):
            n_task += 1
            if task.get('completed') is True:
                comp_tasks.append(task)

    print('Employee {} is done with tasks({}/{}):'
          .format(employee_name, len(comp_tasks), n_task))

    for task in comp_tasks:
        print('\t {}'.format(task.get('title')))


if __name__ == '__main__':
    import requests
    import sys
    if len(sys.argv) == 2:
        get_todo(sys.argv[1])
