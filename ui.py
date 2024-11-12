from Logic import calc,grade_calc,db,login,user
from Logic.Clock import interface

print("Welcome To This App")
name = input("What Is Your Name? \n")
print(f"Well Hello {name}")
#login.record(name, "name")
username = input("Please enter the username you have registed or want to register with. \n")
password_rules= ["Minimum 8 characters",
         "At least one uppercase letter",
         "At least one lowercase letter",
         "At least one number",
         "At least one special character (e.g., !@#$%^&*)",
         "No spaces"
         ]
while True:
    print("Enter a password following these rules")
    for i in range(len(password_rules)):
        print(f"{i+1}. {password_rules[i]}")
    password = input("Enter A Password. \n")
    valid = login.validate_password(password) or False
    if valid:
        break
    print("\033[H\033[J", end="")
    print("The password you entered does not follow the rules")
# python3 ui.py
    
