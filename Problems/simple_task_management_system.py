import threading
import time
import json
import re
from datetime import datetime
from collections import deque
from contextlib import contextmanager
from functools import wraps
from random import choice

# ---------------------------
# Custom Exception Handling
# ---------------------------

class TaskError(Exception):
    """Custom exception for task-related errors."""
    pass

# ---------------------------
# Decorators
# ---------------------------

def logger(func):
    """Decorator to log function calls."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[{datetime.now()}] Function '{func.__name__}' called.")
        return func(*args, **kwargs)
    return wrapper

# ---------------------------
# Context Managers
# ---------------------------

@contextmanager
def file_manager(file_name, mode):
    """Context manager for file operations."""
    f = open(file_name, mode)
    try:
        yield f
    finally:
        f.close()

# ---------------------------
# Generator for Task IDs
# ---------------------------

def task_id_generator():
    """Generates unique task IDs."""
    id = 1
    while True:
        yield f"TASK-{id}"
        id += 1

id_gen = task_id_generator()

# ---------------------------
# Abstract Base Class
# ---------------------------

class Task:
    """Base class for tasks."""
    def __init__(self, title, description):
        self.id = next(id_gen)
        self.title = title
        self.description = description
        self.created_at = datetime.now()
        self.completed = False

    def complete_task(self):
        self.completed = True

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'created_at': self.created_at.isoformat(),
            'completed': self.completed
        }

    def __str__(self):
        status = "Done" if self.completed else "Pending"
        return f"[{self.id}] {self.title} - {status}"

# ---------------------------
# Inheritance and Polymorphism
# ---------------------------

class WorkTask(Task):
    """Task subclass for work-related tasks."""
    def __init__(self, title, description, deadline):
        super().__init__(title, description)
        self.deadline = deadline

    def is_overdue(self):
        return datetime.now() > self.deadline

    def to_dict(self):
        data = super().to_dict()
        data['deadline'] = self.deadline.isoformat()
        return data

class PersonalTask(Task):
    """Task subclass for personal tasks."""
    def __init__(self, title, description, location):
        super().__init__(title, description)
        self.location = location

    def to_dict(self):
        data = super().to_dict()
        data['location'] = self.location
        return data

# ---------------------------
# Task Manager Singleton
# ---------------------------

class TaskManager:
    """Singleton class to manage tasks."""
    _instance = None
    _lock: threading.Lock = threading.Lock()

    def __init__(self):
        self.tasks = []
        self.task_queue = deque()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(TaskManager, cls).__new__(cls)
        return cls._instance

    @logger
    def add_task(self, task):
        if not isinstance(task, Task):
            raise TaskError("Invalid task type.")
        self.tasks.append(task)
        self.task_queue.append(task)
        print(f"Task '{task.title}' added successfully.")

    @logger
    def complete_task(self, task_id):
        task = self.find_task(task_id)
        if task:
            task.complete_task()
            print(f"Task '{task.title}' completed!")
        else:
            print(f"Task with ID '{task_id}' not found.")

    @logger
    def find_task(self, task_id):
        return next((task for task in self.tasks if task.id == task_id), None)

    @logger
    def list_tasks(self, filter_completed=None):
        filtered_tasks = self.tasks
        if filter_completed is not None:
            filtered_tasks = [task for task in self.tasks if task.completed == filter_completed]
        for task in filtered_tasks:
            print(task)

    @logger
    def save_tasks(self, file_name="tasks.json"):
        with file_manager(file_name, 'w') as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)
        print("Tasks saved successfully.")

    @logger
    def load_tasks(self, file_name="tasks.json"):
        try:
            with file_manager(file_name, 'r') as f:
                tasks_data = json.load(f)
                for data in tasks_data:
                    if 'deadline' in data:
                        task = WorkTask(
                            data['title'],
                            data['description'],
                            datetime.fromisoformat(data['deadline'])
                        )
                    elif 'location' in data:
                        task = PersonalTask(
                            data['title'],
                            data['description'],
                            data['location']
                        )
                    else:
                        task = Task(
                            data['title'],
                            data['description']
                        )
                    task.id = data['id']
                    task.created_at = datetime.fromisoformat(data['created_at'])
                    task.completed = data['completed']
                    self.tasks.append(task)
            print("Tasks loaded successfully.")
        except FileNotFoundError:
            print("No saved tasks found.")

# ---------------------------
# Multithreading for Auto-Save
# ---------------------------

def auto_save(manager, interval=60):
    """Auto-saves tasks at specified intervals."""
    while True:
        time.sleep(interval)
        manager.save_tasks()

# ---------------------------
# Regular Expressions Example
# ---------------------------

def validate_task_title(title):
    """Validates task title using regular expressions."""
    pattern = r'^[A-Za-z0-9 ]{3,50}$'
    if re.match(pattern, title):
        return True
    else:
        print("Invalid title. Title should be 3-50 characters long and contain only letters, numbers, and spaces.")
        return False

# ---------------------------
# Main Function
# ---------------------------

@logger
def main():
    manager = TaskManager()

    # Start auto-save thread
    autosave_thread = threading.Thread(target=auto_save, args=(manager, 30), daemon=True)
    autosave_thread.start()

    # Load existing tasks
    manager.load_tasks()

    # Sample tasks using different features
    while True:
        print("\n--- Task Manager ---")
        print("1. Add Work Task")
        print("2. Add Personal Task")
        print("3. Complete Task")
        print("4. List All Tasks")
        print("5. List Pending Tasks")
        print("6. List Completed Tasks")
        print("7. Save and Exit")
        choice_input = input("Choose an option: ")

        try:
            choice_num = int(choice_input)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice_num == 1:
            title = input("Enter task title: ")
            if not validate_task_title(title):
                continue
            description = input("Enter task description: ")
            deadline_input = input("Enter deadline (YYYY-MM-DD): ")
            try:
                deadline = datetime.strptime(deadline_input, "%Y-%m-%d")
                task = WorkTask(title, description, deadline)
                manager.add_task(task)
            except ValueError:
                print("Invalid date format.")
        elif choice_num == 2:
            title = input("Enter task title: ")
            if not validate_task_title(title):
                continue
            description = input("Enter task description: ")
            location = input("Enter task location: ")
            task = PersonalTask(title, description, location)
            manager.add_task(task)
        elif choice_num == 3:
            task_id = input("Enter task ID to complete: ")
            manager.complete_task(task_id)
        elif choice_num == 4:
            manager.list_tasks()
        elif choice_num == 5:
            manager.list_tasks(filter_completed=False)
        elif choice_num == 6:
            manager.list_tasks(filter_completed=True)
        elif choice_num == 7:
            manager.save_tasks()
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
