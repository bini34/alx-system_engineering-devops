import requests
import sys
import csv
"""
export data in the CSV format.
"""


def export_employee_tasks_to_csv(employee_id):

    base_url = "https://jsonplaceholder.typicode.com"

    user_url = f"{base_url}/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    username = user_data.get('username', 'Unknown')

    todos_url = f"{base_url}/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todos_data:
            csv_writer.writerow([employee_id, username,
                                 task['completed'], task['title']])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    export_employee_tasks_to_csv(employee_id)
