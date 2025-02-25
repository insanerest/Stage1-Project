import tkinter as tk
from tkinter import messagebox
import time
import threading
import os
from datetime import datetime


def timerStart():
    root = tk.Tk()
    root.title("World Clock & Timer")
    root.geometry("400x300")

    tk.Label(root, text="Set Timer (seconds):").pack()
    timer_entry = tk.Entry(root)
    timer_entry.pack()
    tk.Button(root, text="Start Timer", command=start_timer).pack()
    timer_label = tk.Label(root, text="")
    timer_label.pack()

    root.mainloop()

    def start_timer():
        try:
            seconds = int(timer_entry.get())
            if seconds <= 0:
                messagebox.showerror("Error", "Enter a valid number of seconds!")
                return
            def countdown():
                nonlocal seconds
                while seconds >= 0:
                    minutes, sec = divmod(seconds, 60)
                    timer_label.config(text=f"Timer: {minutes:02}:{sec:02}")
                    root.update()
                    time.sleep(1)
                    seconds -= 1
                timer_label.config(text="Time's up!")
            threading.Thread(target=countdown, daemon=True).start()
        except ValueError:
            messagebox.showerror("Error", "Enter a valid number!")

