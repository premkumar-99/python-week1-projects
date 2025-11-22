"""
To-Do List Manager (CLI)
Features:
- Add / View / Delete / Mark tasks done
- Persist tasks to a JSON file so tasks survive restarts
- Uses functions to separate IO and logic
"""
import json
import os
from datetime import datetime

DATA_FILE = "tasks_data.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(DATA_FILE, 'w') as f:
        json.dump(tasks, f, indent=2, default=str)

def add_task(tasks, title, tag=None, due_date=None):
    task = {
        "id": (max([t['id'] for t in tasks]) + 1) if tasks else 1,
        "title": title,
        "tag": tag,
        "due_date": due_date,
        "done": False,
        "created_at": datetime.now().isoformat()
    }
    tasks.append(task)
    return task

def list_tasks(tasks, show_all=True):
    if not tasks:
        print("No tasks.")
        return
    for t in tasks:
        status = "✓" if t.get("done") else " "
        print(f"[{status}] {t['id']}. {t['title']} (tag: {t.get('tag')}, due: {t.get('due_date')})")

def delete_task(tasks, task_id):
    for i,t in enumerate(tasks):
        if t['id'] == task_id:
            tasks.pop(i)
            return True
    return False

def mark_done(tasks, task_id):
    for t in tasks:
        if t['id'] == task_id:
            t['done'] = True
            return True
    return False

def menu():
    tasks = load_tasks()
    while True:
        print("\nTo-Do Manager")
        print("1. Add task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Mark task done")
        print("5. Exit")
        choice = input("Choose: ").strip()
        if choice == '1':
            title = input("Title: ").strip()
            tag = input("Tag (optional): ").strip() or None
            due = input("Due date (YYYY-MM-DD) optional: ").strip() or None
            add_task(tasks, title, tag, due)
            save_tasks(tasks)
            print("Added.")
        elif choice == '2':
            list_tasks(tasks)
        elif choice == '3':
            try:
                tid = int(input("Task ID to delete: ").strip())
            except ValueError:
                print("Invalid ID.")
                continue
            if delete_task(tasks, tid):
                save_tasks(tasks)
                print("Deleted.")
            else:
                print("Not found.")
        elif choice == '4':
            try:
                tid = int(input("Task ID to mark done: ").strip())
            except ValueError:
                print("Invalid ID.")
                continue
            if mark_done(tasks, tid):
                save_tasks(tasks)
                print("Marked done.")
            else:
                print("Not found.")
        elif choice == '5':
            print("Bye.")
            return
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    menu()
