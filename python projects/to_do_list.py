import tkinter as tk
from tkinter import messagebox, filedialog

def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    try:
        selected_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def save_tasks():
    tasks = tasks_listbox.get(0, tk.END)
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            for task in tasks:
                file.write(task + "\n")
        messagebox.showinfo("Saved", "Tasks saved successfully.")

def load_tasks():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if file_path:
        tasks_listbox.delete(0, tk.END)
        with open(file_path, "r") as file:
            for line in file:
                tasks_listbox.insert(tk.END, line.strip())

def clear_tasks():
    tasks_listbox.delete(0, tk.END)

root = tk.Tk()
root.title("📝 To-Do List")
root.geometry("400x450")
root.configure(bg="light yellow")

task_entry = tk.Entry(root, font=("Arial", 14), width=25)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=20, command=add_task, bg="green", fg="white")
add_button.pack()

tasks_listbox = tk.Listbox(root, width=40, height=15, font=("Arial", 12), selectbackground="light blue")
tasks_listbox.pack(pady=10)

button_frame = tk.Frame(root, bg="light yellow")
button_frame.pack(pady=10)

tk.Button(button_frame, text="Delete Task", command=delete_task, bg="red", fg="white").grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Save Tasks", command=save_tasks, bg="blue", fg="white").grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Load Tasks", command=load_tasks, bg="purple", fg="white").grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Clear All", command=clear_tasks, bg="dark orange", fg="white").grid(row=0, column=3, padx=5)

root.mainloop()
