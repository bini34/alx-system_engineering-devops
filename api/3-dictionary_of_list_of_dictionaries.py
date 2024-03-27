#!/usr/bin/python3
'''
script to export data in the JSON format
'''
import json
import requests


def export_all_employee_tasks_to_json():
    base_url = "https://jsonplaceholder.typicode.com"

    users_url = f"{base_url}/users"
    users_response = requests.get(users_url)
    users_data = users_response.json()

    all_tasks = {}
    for user in users_data:
        user_id = user['id']
        username = user['username']

        todos_url = f"{base_url}/todos?userId={user_id}"
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        all_tasks[str(user_id)] = [
            {
                "username": username,
                "task": task['title'],
                "completed": task['completed']
            } for task in todos_data
        ]

    json_filename = "todo_all_employees.json"
    with open(json_filename, 'w') as json_file:
        json.dump(all_tasks, json_file)


if __name__ == "__main__":
    export_all_employee_tasks_to_json()
