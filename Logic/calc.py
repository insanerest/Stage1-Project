from Logic.broadcast import broadcast

operators = ["+", "-", "/", "÷", "*", "**"]

def validate_operator(operator):
    if operator in operators:
        return operator
    else:
        return None

def validate_number(number):
    try:
        newNum = float(number)
        if newNum.is_integer():
            return int(newNum)
        else:
            return newNum
    except ValueError:
        return None

def calculate(first, op, second):
    calc = f"{first} {op} {second}"
    answer = round(validate_number(eval(calc)), 2)
    print(f"{calc} = {answer}")

def mainLoop():
    while True:
        inputNum1 = input("First Number: ")
        num1 = validate_number(inputNum1)
        if num1 == None:
            print(f"Invalid Number: {inputNum1}. \n\nPlease Enter A Valid Number\n")
        else:
            break

    while True:
        operator_string = ""
        for oper in operators:
            operator_string = operator_string + " " + oper

        inputOperator = input(
            f"Enter an Operator From The Following:{operator_string} \n"
        )
        operator = validate_operator(inputOperator)
        if operator == None:
            print(
                f"Invalid Operator: {inputOperator}. \n\nPlease Enter A Valid Operator\n"
            )
        else:
            break
    while True:
        inputNum2 = input("Second Number: ")
        num2 = validate_number(inputNum2)
        if num2 == None:
            print(f"Invalid Number: {inputNum1}. \n\nPlease Enter A Valid Number\n")
        else:
            break
    calculate(num1, operator, num2)

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


# python3 calc.py
