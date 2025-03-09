from Logic.Clock import time
from Logic.broadcast import broadcast
def start():
    print("Welcome to the clock app")
    while True:
        print("1. Time")
        print("2. Back")
        choice = input("Enter your choice: ")
        if choice == "1":
            time.timeStart()
        elif choice == "2":
            print("Returning Back")
            broadcast.fire("Choose App")
            return

if __name__ == "__main__":
    while True:
        broadcast.listen("Clock Interface", start)
