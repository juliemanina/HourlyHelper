import tkinter as tk
from tkinter import ttk
import datetime

def calculate_cost():
    global start_time, rate
    rate = float(rate_entry.get())
    start_time = datetime.datetime.now()
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)
    update_time()

def stop_timer():
    global total_cost, rate
    end_time = datetime.datetime.now()
    duration = end_time - start_time
    hours, minutes = divmod(duration.total_seconds(), 3600)
    total_cost = rate * hours + rate * minutes / 60
    result_label.config(text="Total cost: $%.2f" % total_cost)
    stop_button.config(state=tk.DISABLED)
    start_button.config(state=tk.NORMAL)

def update_time():
    current_time = datetime.datetime.now()
    elapsed_time = current_time - start_time
    time_str = str(elapsed_time).split(".")[0]
    time_label.config(text=time_str)
    if start_button["state"] == tk.DISABLED:
        window.after(1000, update_time)  # Update time every second

# Create the main window
window = tk.Tk()
window.title("Babysitter Application")

# Create and place the widgets
rate_label = tk.Label(window, text="Hourly Rate ($):")
rate_label.pack()

rate_entry = tk.Entry(window)
rate_entry.pack()

start_button = tk.Button(window, text="Start", command=calculate_cost)
start_button.pack()

stop_button = tk.Button(window, text="Stop", command=stop_timer, state=tk.DISABLED)
stop_button.pack()

time_label = tk.Label(window, text="00:00:00")
time_label.pack()

result_label = tk.Label(window, text="")
result_label.pack()

# Start the GUI event loop
window.mainloop()
