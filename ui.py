"""

IMPORTANT INFO: 
1. ANY COMMENTED CODE IN THIS FILE IS NOT FUNCTIONAL. REMOVE ALL COMMENTS AFTER ADDING FUNCTIONALITY
2. ANY CODE WITH A COMMENT NEXT TO IT SAYING "#RAF" MEANS: REMOVE THIS CODE AFTER FUNCTIONALITY

"""

from Logic import calc,average_grade_calc as gc,login,user
from Logic.Clock import interface as ci
from Logic import brodcast
import sys

print("Welcome To This App")
name = input("What Is Your Name? \n")
username = None
print(f"Well Hello {name}")
password_rules= ["Minimum 8 characters",
         "At least one uppercase letter",
         "At least one lowercase letter",
         "At least one number",
         "At least one special character (e.g., !@#$%^&*)",
         "No spaces"
         ]
app_options = [
    "Calculator",
    "Grade Calculator",
    "Clock",
    "Quit"
]


def promtApp():
    while True:
        print("Enter a number to get started")
        for i in range(len(app_options)):
            print(f"{i+1}. {app_options[i]}")
        app_option = input("Number\n > ")
        app_option = int(app_option) if app_option.isdigit() else app_option
        if type(app_option) is int and app_option < len(app_options) + 1:
            break
        else:
            print("\n")
            print("INVALID INPUT")
            print("\n")
            print(f"Please Enter a Number From 1 to {len(app_options)}")
    runApp(app_option)

def promptLogin():
    while True:
        global username
        username = input("Please enter the username you have registed or want to register with. \n")
        while True:
            print("Enter a password following these rules")
            for i in range(len(password_rules)):
                print(f"{i+1}. {password_rules[i]}")
            password = input("Enter A Password. \n")
            valid = login.validate_password(password) or False
            #valid = True #RAF
            if valid:
                break
        userData = user.createData(name,username,password)
        isUser = user.isUser(userData.get("username"), "./Logic/data.json")
        #isUser = False #RAF
        if isUser:
            logedIn = user.logIn(userData, "./Logic/data.json")
            #logedIn = True #RAF
            #placeholder = "" #RAF
            if logedIn == True:
                break
            else:
                print("Incorrect Username/Password")
        else:
            user.saveUser(userData, "./Logic/data.json")
            user.logIn(userData, "./Logic/data.json")
            print("Created Account and made Login")
            break
            #placeholder = "" #RAF
    promtApp()

promptLogin()



def calcStart():
    calc.start()

def gcStart():
    gc.start()

def ciStart():
    ci.start()

def runApp(app_num):
    if app_num == 1:
        calcStart()
    if app_num == 2:
        gcStart()
    if app_num == 3:
        ciStart()
    if app_num == 4:
        print(f"Thank you {name} for using this app. We hope you return soon")
        sys.exit(0)

brodcast.listen("Choose App", runApp)

# python3 ui.py

