import tkinter as tk
from tkinter import messagebox
import time

def start_timer():
    try:
        total_seconds = int(hours_entry.get()) * 3600 + int(minutes_entry.get()) * 60 + int(seconds_entry.get())
        if total_seconds > 0:
            countdown(total_seconds)
        else:
            messagebox.showerror("Invalid input", "Please enter a positive time value.")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid integer values for hours, minutes, and seconds.")

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        hrs, mins = divmod(mins, 60)
        timer = f'{hrs:02d}:{mins:02d}:{secs:02d}'
        timer_label.config(text=timer)
        root.update()
        time.sleep(1)
        seconds -= 1
    
    timer_label.config(text="Time's up!")
    messagebox.showinfo("Time's up!", "The countdown has finished!")

root = tk.Tk()
root.title("Countdown Timer")

# Create input fields
hours_label = tk.Label(root, text="Hours:")
hours_label.grid(row=0, column=0)
hours_entry = tk.Entry(root)
hours_entry.grid(row=0, column=1)

minutes_label = tk.Label(root, text="Minutes:")
minutes_label.grid(row=1, column=0)
minutes_entry = tk.Entry(root)
minutes_entry.grid(row=1, column=1)

seconds_label = tk.Label(root, text="Seconds:")
seconds_label.grid(row=2, column=0)
seconds_entry = tk.Entry(root)
seconds_entry.grid(row=2, column=1)

# Create start button
start_button = tk.Button(root, text="Start Timer", command=start_timer)
start_button.grid(row=3, columnspan=2)

# Create timer display
timer_label = tk.Label(root, text="00:00:00", font=('Helvetica', 48))
timer_label.grid(row=4, columnspan=2)

root.mainloop()
