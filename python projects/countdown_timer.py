import time
import os
import sys
import platform

def clear_line():
    sys.stdout.write('\r' + ' ' * 30 + '\r')
    sys.stdout.flush()

def play_ding():
    system = platform.system()
    try:
        if system == "Windows":
            import winsound
            winsound.Beep(1000, 500)
        else:
            print('\a')
    except Exception as e:
        print(f"Could not play sound: {e}")

def countdown(t):
    while t >= 0:
        mins, secs = divmod(t, 60)
        timer = f"{mins:02d}:{secs:02d}"
        clear_line()
        print(f"⏳ Time left: {timer}", end='', flush=True)
        time.sleep(1)
        t -= 1
    clear_line()
    print("✅ Time is up!")
    play_ding()

try:
    t = int(input("Enter countdown time in seconds: "))
    countdown(t)
except ValueError:
    print("❌ Please enter a valid number.")
