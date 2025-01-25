def validate_password(password):
    special =  "!@#$%^&*()_+[]{}|;:',.<>?/"
    valid = True
    errors = ""

    if len(password) < 8:
        valid = False
        errors += "Password Must Contain 8 Charecters Or More \n"
    
    has_uppercase = False
    has_lowercase = False
    has_space = False
    has_number = False
    has_special = False
    for char in password:
        char = str(char)
        if char == char.upper() and not char == " ":
            has_uppercase = True
        if char == char.lower() and not char == " ":
            has_lowercase = True
        if char.isdigit():
            has_number = True
        if char == " ":
            has_space = True
        for s in special:
            if char == s:
                has_special = True


    if not has_lowercase or not has_uppercase:
        valid = False
        errors += "Password Must Contain Uppercase And Lowercase Letter \n"
    if not has_number:
        valid = False
        errors += "Password Must Have A Number \n"
    if has_space:
        valid = False
        errors += "Password Must Not Contain Spaces \n"
    if not has_special:
        valid = False
        errors += "Password Must Contain A Special Charecter \n"

    print("\033[H\033[J", end="")
    print(errors)
    return valid




# python3 login.py

    

    
    
