import tkinter as tk
from tkinter import messagebox
import re
from datetime import datetime

def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def is_valid_dob(dob):
    try:
        datetime.strptime(dob, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def submit_form():
    fname = entry_fname.get().strip()
    lname = entry_lname.get().strip()
    dob = entry_dob.get().strip()
    email = entry_email.get().strip()
    if not (fname and lname and dob and email):
        messagebox.showerror("Error", "All fields are required.")
        return
    if not is_valid_dob(dob):
        messagebox.showerror("Invalid DOB", "Date of Birth must be in YYYY-MM-DD format.")
        return
    if not is_valid_email(email):
        messagebox.showerror("Invalid Email", "Please enter a valid email address (e.g., user@example.com).")
        return
    messagebox.showinfo("Success", "Registration Successful!")
    print("----- Registered Info -----")
    print("First Name:", fname)
    print("Last Name:", lname)
    print("DOB:", dob)
    print("Email:", email)

def reset_form():
    entry_fname.delete(0, tk.END)
    entry_lname.delete(0, tk.END)
    entry_dob.delete(0, tk.END)
    entry_email.delete(0, tk.END)

root = tk.Tk()
root.title("Registration Form")
root.geometry("400x400")
root.configure(bg="#e6f2ff")

tk.Label(root, text="Registration Form", font=("Arial", 16, "bold"), bg="#e6f2ff").pack(pady=10)
tk.Label(root, text="First Name", bg="#e6f2ff").pack()
entry_fname = tk.Entry(root, width=30)
entry_fname.pack()
tk.Label(root, text="Last Name", bg="#e6f2ff").pack()
entry_lname = tk.Entry(root, width=30)
entry_lname.pack()
tk.Label(root, text="Date of Birth (YYYY-MM-DD)", bg="#e6f2ff").pack()
entry_dob = tk.Entry(root, width=30)
entry_dob.pack()
tk.Label(root, text="Email", bg="#e6f2ff").pack()
entry_email = tk.Entry(root, width=30)
entry_email.pack()
tk.Button(root, text="Submit", command=submit_form, bg="green", fg="white", width=15).pack(pady=10)
tk.Button(root, text="Reset", command=reset_form, bg="red", fg="white", width=15).pack()

root.mainloop()
