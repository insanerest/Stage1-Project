"""

IMPORTANT INFO: 
1. ANY COMMENTED CODE IN THIS FILE IS NOT FUNCTIONAL. REMOVE ALL COMMENTS AFTER ADDING FUNCTIONALITY
2. ANY CODE WITH A COMMENT NEXT TO IT SAYING "#RAF" MEANS: REMOVE THIS CODE AFTER FUNCTIONALITY

"""

from Logic import calc,grade_calc as gc,db,login,user
from Logic.Clock import interface as ci
import sys

print("Welcome To This App")
name = input("What Is Your Name? \n")
print(f"Well Hello {name}")
username = input("Please enter the username you have registed or want to register with. \n")
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
    "Notes",
    "Clock",
    "Quit"
]
while True:
    print("Enter a password following these rules")
    for i in range(len(password_rules)):
        print(f"{i+1}. {password_rules[i]}")
    password = input("Enter A Password. \n")
    #valid = login.validate_password(password) or False
    valid = True #RAF
    if valid:
        break
    print("\033[H\033[J", end="")
    print("The password you entered does not follow the rules")
#userData = user.createData(name,username,password)
#isUser = user.isUser(userData.username)
isUser = False
if isUser:
    #user.logIn(userData)
    placeholder = "" #RAF
else:
    #user.saveUser(userData)
    #user.logIn(userData)
    placeholder = "" #RAF

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

def runApp(app_num):
    if app_num == 1:
        calc.start()
    if app_num == 2:
        gc.start()
    if app_num == 3:
        db.start()
    if app_num == 4:
        ci.start()
    if app_num == 5:
        print(f"Thank you {name} for using this app. We hope you return soon")
        sys.exit(0)


#runApp(app_option)

# python3 ui.py

