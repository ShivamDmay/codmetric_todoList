import tkinter as tk
from tkinter import messagebox
import os

FILE_NAME = "tasks.txt" """File where tasks get saved"""

def load_tasks():
    """Loads tasks from the file"""
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return [line.strip() for line in file.readlines()]

def save_tasks():
    """Saves tasks to the file"""
    with open(FILE_NAME, "w") as file:
        file.writelines("\n".join(tasks))

def add_task():
    """Adds a task to the list"""
    task = task_entry.get().strip()
    if task:
        tasks.append(task + " [Pending]")
        save_tasks()
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    """Deletes the selected task"""
    try:
        selected_index = task_listbox.curselection()[0]
        del tasks[selected_index]
        save_tasks()
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task first!")

def mark_completed():
    """Marks a task as completed"""
    try:
        selected_index = task_listbox.curselection()[0]
        task = tasks[selected_index]
        if "[Pending]" in task:
            tasks[selected_index] = task.replace("[Pending]", "[Completed]")
            save_tasks()
            update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Select a task first!")

def update_listbox():
    """Updates the listbox display"""
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

tasks = load_tasks()

"""Tkninter gui"""
root = tk.Tk()
root.title("To-Do List Manager")
root.geometry("400x400")

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=30)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

mark_button = tk.Button(root, text="Mark Completed", command=mark_completed)
mark_button.pack()

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

update_listbox()

root.mainloop()
