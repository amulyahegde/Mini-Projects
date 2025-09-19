tasks = []  # list to store tasks

def show_menu():
    print("\nTo-Do List")
    print("1. View list")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        if not tasks:
            print("\nNo tasks")
        else:
            print("Your tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")

    elif choice == "2":
        task = input("Enter a new task: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "3":
        if not tasks:
            print("No tasks to remove")
        else:
            print("Your tasks:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            try:
                task_num = int(input("Enter task number to remove: "))
                removed = tasks.pop(task_num - 1)
                print(f"Removed: {removed}")
            except (ValueError, IndexError):
                print("Invalid task number.")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice, try again")
 