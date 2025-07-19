import tkinter as tk
import os
import json

from tkinter import messagebox

tasks = []
TASK_FILE = "tasks.json"

def save_tasks():
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f)

def load_tasks():
    global tasks
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'r') as f:
            tasks = json.load(f)

def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "You must enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        tasks.pop(selected)
        update_listbox()
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to delete!")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)
        def save_tasks():
            with open(TASK_FILE, 'w') as f:
                json.dump(tasks, f)
        def load_tasks():
            global tasks
            if os.path.exists(TASK_FILE):
                with open(TASK_FILE, 'r') as f:
                    tasks = json.load(f)        

# Setup window
window = tk.Tk()
window.title("My To-Do List")
window.geometry("300x400")

# Widgets
entry = tk.Entry(window, width=30)
entry.pack(pady=10)

add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

listbox = tk.Listbox(window, width=45, height=15)
listbox.pack(pady=10)

# Run the app
load_tasks()
update_listbox()

window.mainloop()
