#!/usr/bin/python3
"""REST API Rest api - Returns to-do list information for a given employee ID."""
import json
import requests
import sys

def return_todo_list(employee_id):
    """Returns a list of to dos for an employee."""
    url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    res = requests.get(url)
    to_do_list = json.loads(res.text)
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_res = requests.get(user_url)
    user_details = json.loads(user_res.text)
    tasks = len(to_do_list)
    tasks_complete = [task for task in to_do_list if task["completed"] is True]
    complete = len(tasks_complete)
    print("Employee {} is done with tasks({}/{}):".format(user_details["name"], complete, tasks))
    for n in tasks_complete:
        print("\t{}".format(n["title"]))
if __name__ == "__main__":
    if len(sys.argv) !=2:
        print("Please provide a userID")
    else:
        try:
            id = int(sys.argv[1])
        except Exception:
            print("Please privide a valid input")
    return_todo_list(id)
    
