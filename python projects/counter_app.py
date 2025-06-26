import tkinter as tk
from tkinter import messagebox, ttk
import os
import platform
import datetime

counter = 0
running = False
mode_type = "count_up"
min_limit = 0
max_limit = 100
save_file = "counter_value.txt"
dark_theme = False
countdown_to_time = None

if os.path.exists(save_file):
    with open(save_file, "r") as file:
        try:
            counter = int(file.read().strip())
        except ValueError:
            counter = 0

def play_alert():
    system = platform.system()
    try:
        if system == "Windows":
            import winsound
            winsound.Beep(1000, 500)
        else:
            print("\a")
    except Exception as e:
        print(f"Sound error: {e}")

def update_counter():
    global counter
    if running:
        if countdown_to_time and mode_type == "countdown":
            remaining = int((countdown_to_time - datetime.datetime.now()).total_seconds())
            if remaining >= 0:
                counterLabel.config(text=str(remaining))
                progressBar['value'] = 100 - (remaining / max(1, total_seconds)) * 100
                percentLabel.config(text=f"{int(progressBar['value'])}%")
                counterLabel.after(1000, update_counter)
            else:
                play_alert()
                stop()
        else:
            if mode_type == "countdown":
                if counter > min_limit:
                    counter -= 1
                else:
                    play_alert()
                    stop()
            else:
                if counter < max_limit:
                    counter += 1
                else:
                    counter = max_limit
                    play_alert()
                    stop()
            update_display()
            counterLabel.after(1000, update_counter)

def update_display():
    counterLabel.config(text=str(counter))
    progress = 100 * (counter - min_limit) / (max_limit - min_limit) if max_limit > min_limit else 0
    progress = min(progress, 100)
    progressBar['value'] = progress
    percentLabel.config(text=f"{int(progress)}%")
    if int(progress) == 100:
        play_alert()

def start():
    global running
    running = True
    startButton.config(state="disabled")
    update_counter()

def stop():
    global running
    running = False
    startButton.config(state="normal")

def reset():
    global counter, countdown_to_time
    countdown_to_time = None
    counter = 0
    update_display()
    startButton.config(state="normal")

def toggle_mode():
    global mode_type, countdown_to_time
    if mode_type == "count_up":
        mode_type = "countdown"
    elif mode_type == "countdown":
        mode_type = "stopwatch"
    else:
        mode_type = "count_up"
    countdown_to_time = None
    modeButton.config(text=f"Mode: {mode_type.capitalize()}")

def save_value():
    with open(save_file, "w") as file:
        file.write(str(counter))

def apply_limits():
    global min_limit, max_limit, counter
    try:
        new_min = int(minEntry.get())
        new_max = int(maxEntry.get())
        if new_min >= new_max:
            raise ValueError
        min_limit = new_min
        max_limit = new_max
        counter = max(min(counter, max_limit), min_limit)
        update_display()
    except ValueError:
        messagebox.showerror("Invalid Input", "Min must be less than Max and both must be integers.")

def toggle_theme():
    global dark_theme
    dark_theme = not dark_theme
    bg = "black" if dark_theme else "white"
    fg = "white" if dark_theme else "black"
    def apply_theme(widget):
        if isinstance(widget, (tk.Frame, tk.Label, tk.Button, tk.Entry)):
            widget.configure(bg=bg)
            if isinstance(widget, (tk.Label, tk.Button)):
                widget.configure(fg=fg)
            elif isinstance(widget, tk.Entry):
                widget.configure(fg=fg, insertbackground=fg)
        for child in widget.winfo_children():
            apply_theme(child)
    apply_theme(window)
    window.configure(bg=bg)
    themeButton.config(text="Theme: Light" if dark_theme else "Theme: Dark")

def set_datetime_countdown():
    global countdown_to_time, total_seconds
    try:
        target = f"{dateEntry.get()} {timeEntry.get()}"
        countdown_to_time = datetime.datetime.strptime(target, "%Y-%m-%d %H:%M:%S")
        now = datetime.datetime.now()
        total_seconds = (countdown_to_time - now).total_seconds()
        if total_seconds <= 0:
            raise ValueError
        start()
    except ValueError:
        messagebox.showerror("Invalid Format", "Enter date and time in format:\nYYYY-MM-DD HH:MM:SS")

window = tk.Tk()
window.title("Counter App")
window.geometry("500x550")
window.configure(bg='white')

counterLabel = tk.Label(window, text=str(counter), fg='black', bg='green', font=("Arial", 24))
counterLabel.pack(pady=20)

progressBar = ttk.Progressbar(window, orient="horizontal", length=300, mode="determinate")
progressBar.pack()
percentLabel = tk.Label(window, text="0%", bg="white", fg="black")
percentLabel.pack(pady=5)

btn_frame = tk.Frame(window, bg='white')
btn_frame.pack(pady=10)

startButton = tk.Button(btn_frame, text="Start", bg="red", fg="black", command=start)
startButton.grid(row=0, column=0, padx=5, ipadx=10)

tk.Button(btn_frame, text="Stop", bg="red", fg="black", command=stop).grid(row=0, column=1, padx=5, ipadx=10)
tk.Button(btn_frame, text="Reset", bg="red", fg="black", command=reset).grid(row=0, column=2, padx=5, ipadx=10)

modeButton = tk.Button(window, text="Mode: Count_up", bg="orange", fg="black", command=toggle_mode)
modeButton.pack(pady=5)

saveButton = tk.Button(window, text="Save", bg="blue", fg="white", command=save_value)
saveButton.pack(pady=5)

themeButton = tk.Button(window, text="Theme: Dark", bg="gray", fg="white", command=toggle_theme)
themeButton.pack(pady=5)

limitFrame = tk.Frame(window, bg='white')
limitFrame.pack(pady=10)

tk.Label(limitFrame, text="Min:", bg='white').grid(row=0, column=0)
minEntry = tk.Entry(limitFrame, width=5)
minEntry.insert(0, str(min_limit))
minEntry.grid(row=0, column=1)

tk.Label(limitFrame, text="Max:", bg='white').grid(row=0, column=2)
maxEntry = tk.Entry(limitFrame, width=5)
maxEntry.insert(0, str(max_limit))
maxEntry.grid(row=0, column=3)

tk.Button(limitFrame, text="Apply Limits", command=apply_limits, bg="dark green", fg="white").grid(row=0, column=4, padx=10)

datetimeFrame = tk.Frame(window, bg='white')
datetimeFrame.pack(pady=10)

tk.Label(datetimeFrame, text="Countdown to (YYYY-MM-DD):", bg="white").grid(row=0, column=0)
dateEntry = tk.Entry(datetimeFrame, width=10)
dateEntry.grid(row=0, column=1)

tk.Label(datetimeFrame, text="HH:MM:SS:", bg="white").grid(row=0, column=2)
timeEntry = tk.Entry(datetimeFrame, width=8)
timeEntry.grid(row=0, column=3)

tk.Button(datetimeFrame, text="Start Timer", bg="purple", fg="white", command=set_datetime_countdown).grid(row=0, column=4, padx=10)

window.mainloop()
