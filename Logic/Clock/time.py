import tkinter as tk
from tkinter import messagebox
import os
from datetime import datetime, timedelta
from Logic.broadcast import broadcast

def mainLoop():
    def get_time():
        city_time_offsets = {
            "New York": -5,  # EST (UTC-5)
            "Los Angeles": -8,  # PST (UTC-8)
            "London": 0,  # UTC+0
            "Tokyo": 9,  # JST (UTC+9)
            "Delhi": 5.5,  # IST (UTC+5:30)
            "Cairo": 2,  # EET (UTC+2)
            "Mecca": 3,  # AST (UTC+3)
        }
        city = city_entry.get().strip()
        if not city:
            messagebox.showwarning("Warning", "Please enter a city name.")
            return

        if city not in city_time_offsets:
            messagebox.showerror("Error", f"Timezone for '{city}' not found.")
            return

        try:
            # Get UTC time
            utc_time = datetime.utcnow()

            # Get the offset for the entered city
            offset_hours = city_time_offsets[city]
            offset_delta = timedelta(
                hours=int(offset_hours), minutes=(offset_hours % 1) * 60
            )

            # Convert to local city time
            city_time = utc_time + offset_delta

            # Display the correct time
            time_label.config(
                text=f"Time in {city}: {city_time.strftime('%H:%M:%S')} (UTC{offset_hours:+})"
            )

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

def timeStart():
    while True:
        print("1. Get Time")
        print("2. Back")
        choice = input("Enter your choice: ")
        if choice == "1":
            mainLoop()
        elif choice == "2":
            print("Returning Back")
            broadcast.fire("Clock Interface")
            return
