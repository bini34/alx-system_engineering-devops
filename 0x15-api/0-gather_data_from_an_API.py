#!/usr/bin/python3
"""
using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys


def get_employee_todo_list_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name', 'Unknown')

    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    completed_tasks = sum(task['completed'] for task in todos_data)

    print(f"Employee {employee_name} is done with tasks({completed_tasks}")
    print("/{total_tasks}):")
    for task in todos_data:
        if task['completed']:
            print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)
    get_employee_todo_list_progress(employee_id)
