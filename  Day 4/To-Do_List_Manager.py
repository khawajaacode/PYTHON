todo_list = []

def display_task():
    if len(todo_list) == 0:
        print("Your todo list is empty")
    else:
        print("Your Todo List:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")

def add_task():
    task = input("Enter your task: ")
    todo_list.append(task)
    print(f"TASK ADDED: {task}")

def remove_task():
    if len(todo_list) == 0:
        print("Your todo list is empty, nothing to remove.")
    else:
        task = input("Enter your task to remove: ")
        if task in todo_list:
            todo_list.remove(task)
            print(f"TASK REMOVED: {task}")
        else:
            print(f"TASK '{task}' not found in the list.")

def main():
    while True:
        print("\nTodo list Manager")
        print("1. Display task")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            display_task()
        elif choice == "2":
            add_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Bye")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
