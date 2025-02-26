import tkinter as tk
from tkinter import messagebox
import time
import threading
import os
from datetime import datetime

def timeStart():
    def get_time():
        city = city_entry.get()
        if not city:
            messagebox.showwarning("Warning", "Please enter a city name.")
            return
        try:
            timezone = os.popen("date +%Z").read().strip()
            city_time = datetime.now()
            time_label.config(text=f"Time in {city}: {city_time.strftime('%H:%M:%S')} ({timezone})")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    root = tk.Tk()
    root.title("World Clock & Timer")
    root.geometry("400x300")

    tk.Label(root, text="Enter City:").pack()
    city_entry = tk.Entry(root)
    city_entry.pack()
    tk.Button(root, text="Get Time", command=get_time).pack()
    time_label = tk.Label(root, text="")
    time_label.pack()
    root.mainloop()