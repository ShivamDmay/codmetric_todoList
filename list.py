import os

FILE_NAME = "tasks.txt"

def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks():
    with open(FILE_NAME, "w") as file:
        file.writelines("\n".join(tasks))

def show_tasks():
    print("\n--- TO-DO LIST ---")
    if not tasks:
        print("No tasks yet!")
    else:
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    print("------------------\n")

def add_task():
    task = input("Enter new task: ").strip()
    if task:
        tasks.append(task + " [Pending]")
        save_tasks()
        print("Task added.")
    else:
        print("Task cannot be empty!")

def delete_task():
    show_tasks()
    try:
        index = int(input("Enter task number to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            save_tasks()
            print(f"Deleted: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_completed():
    show_tasks()
    try:
        index = int(input("Enter task number to mark completed: "))
        if 1 <= index <= len(tasks):
            if "[Pending]" in tasks[index - 1]:
                tasks[index - 1] = tasks[index - 1].replace("[Pending]", "[Completed]")
                save_tasks()
                print("Task marked as completed.")
            else:
                print("Task is already completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main_menu():
    while True:
        print("\n1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_completed()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    tasks = load_tasks()
    main_menu()
