def display_menu():
    print("To-Do List Menu:")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Exit")

def view_tasks(tasks):
    if not tasks:
        print("No tasks.")
    else:
        print("Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added.")

def complete_task(tasks):
    view_tasks(tasks)
    if tasks:
        task_number = int(input("Enter task number to complete: "))
        if 1 <= task_number <= len(tasks):
            completed_task = tasks.pop(task_number - 1)
            print(f"Task '{completed_task}' completed.")
        else:
            print("Invalid task number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
