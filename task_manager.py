# task_manager.py

tasks = []

def add_task():
    task = input("Enter task: ").strip()
    if task:
        tasks.append({"task": task, "done": False})
        print("✅ Task added.")
    else:
        print("⚠️ Task cannot be empty.")

def view_tasks():
    if not tasks:
        print("📭 No tasks found.")
    else:
        print("\n📝 Your Tasks:")
        for idx, task in enumerate(tasks, start=1):
            status = "✔ Done" if task["done"] else "✘ Not Done"
            print(f"{idx}. {task['task']} [{status}]")

def complete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print("✅ Task marked as done.")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"🗑️ Deleted task: {removed['task']}")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")

def menu():
    while True:
        print("\n==== Task Manager ====")
        print("1. Add Task\n2. View Tasks\n3. Complete Task\n4. Delete Task\n5. Exit")
        choice = input("Choose an option (1-5): ").strip()
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("👋 Exiting Task Manager. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice.")

if __name__ == "__main__":
    menu()
from datetime import datetime

def complete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            completed_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            tasks[index]["completed_at"] = completed_time
            print(f"✅ Task marked as done at {completed_time}")
        else:
            print("⚠️ Invalid task number.")
    except ValueError:
        print("⚠️ Please enter a valid number.")
