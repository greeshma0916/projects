from tkinter import *
import datetime
import time
import winsound
import threading

def alarm(set_alarm_timer):
    alarm_hour, alarm_min, alarm_sec = map(int, set_alarm_timer.split(":"))
    now = datetime.datetime.now()
    alarm_time = now.replace(hour=alarm_hour, minute=alarm_min, second=alarm_sec, microsecond=0)
    if alarm_time <= now:
        alarm_time += datetime.timedelta(days=1)
    while datetime.datetime.now() < alarm_time:
        time.sleep(1)
    for _ in range(3):
        winsound.Beep(1000, 500)
        time.sleep(0.5)

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    t = threading.Thread(target=alarm, args=(set_alarm_timer,))
    t.start()

clock = Tk()
clock.title("Simple Alarm Clock")
clock.geometry("400x200")
clock.configure(bg="light yellow")

Label(clock, text="When to wake you up", fg="blue", relief="solid",
      font=("Helvetica", 7, "bold")).place(x=0, y=5)

Label(clock, text="Hour  Min   Sec", font=60).place(x=110, y=30)
Label(clock, text="Enter time in 24-hour format!", fg="red",
      bg="black", font="Arial").place(x=60, y=120)

hour = StringVar()
min = StringVar()
sec = StringVar()

Entry(clock, textvariable=hour, bg="pink", width=15).place(x=110, y=50)
Entry(clock, textvariable=min, bg="pink", width=15).place(x=150, y=50)
Entry(clock, textvariable=sec, bg="pink", width=15).place(x=200, y=50)

Button(clock, text="Set Alarm", fg="red", width=10, command=actual_time).place(x=150, y=80)

clock.mainloop()
