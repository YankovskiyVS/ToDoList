'''
This is a concole app, that can make your everyday task management easier.
Add and delete tasks to your own list. If you want to start over - just clear the list.
When the task is done - use the "mark" option, so you can control^ what is done.
Fast and easy
bash script for starting the code is available, check the GitHub for more
'''

import json
import os

TASK_FILE = "Tasks.json"  # File to save tasks

# Ensure the file exists
def ensure_json_file():
    '''Function to Ensure the file exists'''
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, "w", encoding = "utf-8") as file:
            json.dump([], file, indent=4)  # Create an empty list in the file
        print(f"Created {TASK_FILE}.")
    else:
        print("Opening your tasks...")

# Load tasks from the file
def load_tasks():
    '''Function to load data from the file'''
    try:
        with open(TASK_FILE, "r", encoding = "utf-8") as file:
            tasks = json.load(file)
            print("Your current tasks:")
            list_tasks(tasks)
            return tasks
    except FileNotFoundError:
        print("Task file not found. Creating a new one.")
        return []
    except json.JSONDecodeError:
        print("Task file is corrupted. Starting with an empty list.")
        return []

# Save tasks to the file
def save_tasks(tasks):
    '''Function to save data to the file'''
    try:
        with open(TASK_FILE, "w", encoding = "utf-8") as file:
            json.dump(tasks, file, indent=4)
    except SystemError as e:
        print(f"Error saving tasks: {e}")

# List the tasks
def list_tasks(tasks):
    '''Function to show the task list'''
    print("\nTo-do list:")
    if not tasks:
        print("No tasks were found.")
        return
    for index, task in enumerate(tasks, start=1):
        status = "[X]" if task["completed"] else "[ ]"
        print(f"{index}. {status} {task['task']}")

# Add a new task
def add_tasks(tasks):
    '''Function to add the new task in the list'''
    try:
        add_confirm = input("\nDo you want to add the task? (Y/N): ")
        if add_confirm.upper() == "Y":
            task_name = input("Enter your task: ")
            if task_name.strip():  # Ensure the task name is not empty
                tasks.append({"task": task_name, "completed": False})
                print(f"Task '{task_name}' added to the list")
            else:
                print("Task name cannot be empty.")
        else:
            print("Task was not added to the list")
    except SystemError as e:
        print(f"An error occurred while adding the task: {e}")

# Delete a task
def delete_task(tasks):
    '''Function to delete an existing task from the list'''
    list_tasks(tasks)
    try:
        delete_confirm = input("\nDo you want to delete the task? (Y/N): ")
        if delete_confirm.upper() == "Y":
            task_num = int(input("\nEnter the task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task['task']}' deleted.")
            else:
                print("Invalid task number.")
        else:
            print("Task was not deleted")
    except SystemError as e:
        print(f"An error occurred while deleting the task: {e}")

#Clear the task list
def clear_list(tasks):
    '''Function to delete all tasks from the list'''
    list_tasks(tasks)
    try:
        clear_confirm = input("\nDo you want to clear the task list? (Y/N): ")
        if clear_confirm.upper() == "Y":
            tasks.clear()
        else:
            print("Task list was not cleared")
    except SystemError:
        print("Task list was not cleared")

# Mark a task as completed
def complete_tasks(tasks):
    '''Function to mark the completed task'''
    list_tasks(tasks)
    try:
        complete_confirm = input("\nDo you want to complete the task? (Y/N): ")
        if complete_confirm.upper() == "Y":
            task_num = int(input("\nEnter the task number to mark as completed: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]["completed"] = True
                print(f"Task '{tasks[task_num - 1]['task']}' marked as completed.")
            else:
                print("Invalid task number.")
        else:
            print("Task was not completed")
    except SystemError as e:
        print(f"Task was not completed. Error: {e}")

# Main function
def main():
    '''Main function'''
    ensure_json_file()  # Ensure the tasks file exists first
    tasks = load_tasks()  # Then load tasks from the file
    while True:
        print("\nTo-do list app")
        print("\n1. List Tasks")
        print("\n2. Add Task")
        print("\n3. Mark Task as Completed")
        print("\n4. Delete Task")
        print("\n5. Clear Task list")
        print("\n6. Exit\n")
        #Choose between options
        choice = input("Choose an option: ")
        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            add_tasks(tasks)
        elif choice == "3":
            complete_tasks(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            clear_list(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
