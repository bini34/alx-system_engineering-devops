import requests
import sys

def get_employee_todo_list_progress(employee_id):
    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetching user information
    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name', 'Unknown')

    # Fetching TODO list information
    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculating TODO list progress
    total_tasks = len(todos_data)
    completed_tasks = sum(task['completed'] for task in todos_data)

    # Printing the progress
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for task in todos_data:
        if task['completed']:
            print(f"\t {task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_list_progress(employee_id)

