#!/usr/bin/python3
"""Extend your Python script to export data in the Json format."""


def export_to_json(users_id):
    """what you did in the task #0"""
    todo_url = 'http://jsonplaceholder.typicode.com/todos'
    user_url = 'http://jsonplaceholder.typicode.com/users/{}'.format(
        users_id)
    user_employ = requests.get(user_url)
    to_do = requests.get(todo_url)

    """get information"""
    employee_name = user_employ.json().get('username')
    n_task, comp_tasks = 0, []
    for task in to_do.json():
        if task.get('userId') == int(users_id):
            comp_tasks.append(task)

    """open file of json and add data"""
    with open("{}.json".format(users_id), mode="w") as fd:
        """Write in the file user_id.json"""

        write_file = {users_id: []}
        for obj in comp_tasks:
            new_obj = {
                'task': obj.get('title'),
                'completed': obj.get('completed'),
                'username': employee_name
            }
            write_file[users_id].append(new_obj)
        json.dump(write_file, fd)


if __name__ == '__main__':
    import json
    import requests
    import sys
    if len(sys.argv) == 2:
        export_to_json(sys.argv[1])
