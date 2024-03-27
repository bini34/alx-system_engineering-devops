#!/usr/bin/python3
"""
export data in the JSON format
"""
import Json
import requests
import sys


def export_employee_tasks_to_json(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get('username', 'Unknown')

    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    tasks = []
    for task in todos_data:
        tasks.append({
            "task": task['title'],
            "completed": task['completed'],
            "username": username
        })

    json_filename = f"{employee_id}.json"
    with open(json_filename, 'w') as json_file:
        json.dump({str(employee_id): tasks}, json_file)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    export_employee_tasks_to_json(employee_id)
