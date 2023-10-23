#!/usr/bin/python3
"""
Script that, using this REST API, for a given employee ID, returns
information about his/her TODO list progress
"""

import json
import requests

def get_employee_todo_list_progress(employee_id):
  """Returns information about an employee's TODO list progress.

  Args:
    employee_id: The ID of the employee.

  Returns:
    A dictionary containing the following information:
      - employee_name: The name of the employee.
      - number_of_done_tasks: The number of completed tasks.
      - total_number_of_tasks: The total number of tasks.
      - completed_task_titles: A list of the titles of completed tasks.
  """

  # Get the employee's TODO list.
  response = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={employee_id}')
  todo_list = json.loads(response.content)

  # Count the number of completed and non-completed tasks.
  number_of_done_tasks = 0
  total_number_of_tasks = 0
  for task in todo_list:
    if task['completed']:
      number_of_done_tasks += 1
    total_number_of_tasks += 1

  # Get the titles of completed tasks.
  completed_task_titles = []
  for task in todo_list:
    if task['completed']:
      completed_task_titles.append(task['title'])

  # Return a dictionary containing the information we gathered.
  return {
    'employee_name': todo_list[0]['user']['name'],
    'number_of_done_tasks': number_of_done_tasks,
    'total_number_of_tasks': total_number_of_tasks,
    'completed_task_titles': completed_task_titles
  }

def main():
  """Prints the TODO list progress of an employee to the standard output."""

  employee_id = int(input('Enter employee ID: '))

  employee_todo_list_progress = get_employee_todo_list_progress(employee_id)

  print(f'Employee {employee_todo_list_progress["employee_name"]} is done with tasks({employee_todo_list_progress["number_of_done_tasks"]}/{employee_todo_list_progress["total_number_of_tasks"]}):')
  for task_title in employee_todo_list_progress['completed_task_titles']:
    print(f'\t{task_title}')

if __name__ == '__main__':
