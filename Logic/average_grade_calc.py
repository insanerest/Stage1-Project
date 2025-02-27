from Logic.broadcast import broadcast
subject_grades = []

def validate_number(number):
    try:
        newNum = float(number)
        if newNum.is_integer():
            return int(newNum)
        else:
            return newNum
    except ValueError:
        return None

def calculate(grades, count):
    total = 0
    for grade in grades:
        total = total + grade
    answer = round(total / count, 2)
    print(f"Your average grade for all subjects is {answer}")

def mainLoop():
    while True:
        subjects = input("How many subjects do you have: ")
        subjects = validate_number(subjects)
        if not subjects:
            print(
                f"Invalid Number: {subjects}\n Please enter a valid number. 0 does not count"
            )
        else:
            break
    for subject in range(subjects):
        while True:
            inputSubject_grade = input(f"Subject Number {subject+1}'s Grade: ")
            subject_grade = validate_number(inputSubject_grade)
            if not subject_grade:
                print(
                    f"Invalid Number: {inputSubject_grade}\nPlease enter a valid number. 0 does not count"
                )
            else:
                break
        subject_grades.append(subject_grade)
    calculate(subject_grades, subjects)

def start():
    while True:
        print("1. Calculate")
        print("2. Back")
        choice = input("Enter your choice: ")
        if choice == "1":
            mainLoop()
        elif choice == "2":
            print("Returning Back")
            broadcast.fire("Choose App")
            return

# python3 grade_calc.py
