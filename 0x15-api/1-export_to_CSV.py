#!/usr/bin/python3
"""Extend your Python script to export data in the CSV format."""


def export_to_csv(users_id):
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

    """open file of csv and add data"""
    with open("{}.csv".format(users_id), mode="w", newline='') as fd:
        """Write in the file user_id.csv"""
        write_file = csv.writer(fd, quoting=csv.QUOTE_NONNUMERIC)
        for obj in comp_tasks:
            row = ["{}".format(users_id), "{}".format(employee_name),
                   "{}".format(obj.get('completed')),
                   "{}".format(obj.get('title'))]
            write_file.writerow(row)


if __name__ == '__main__':
    import csv
    import requests
    import sys
    if len(sys.argv) == 2: 
        export_to_csv(sys.argv[1])
