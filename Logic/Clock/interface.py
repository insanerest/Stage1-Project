from Logic.Clock import time, timer
from Logic.broadcast import broadcast
def start():
    print("Welcome to the clock app")
    while True:
        print("1. Time")
        print("2. Timer")
        print("3. Back")
        choice = input("Enter your choice: ")
        if choice == "1":
            time.timeStart()
        elif choice == "2":
            timer.timerStart()
        elif choice == "3":
            print("Returning Back")
            broadcast.fire("Choose App")
            return

if __name__ == "__main__":
    while True:
        broadcast.listen("Clock Interface", start)
