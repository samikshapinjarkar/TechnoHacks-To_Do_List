tasks = []

def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("\nTo-Do List:")

        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a task: ").strip()
    if task:
        tasks.append(task)
        print("Task added!")

def remove_task():
    show_tasks()
    try:
        index = int(input("Enter task number to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    print("\nOptions: (1) View Tasks (2) Add Task (3) Remove Task (4) Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again.")
