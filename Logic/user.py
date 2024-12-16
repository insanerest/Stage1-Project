import json

def createData(name,username,password):
    return {
        "name":name,
        "username":username,
        "password":password
    }

def isUser(username, JSONpath):
    with open(JSONpath, "r") as jsonFile:
        jsonData = json.load(jsonFile)
        for user in jsonData:
            if user.get("username") == username:
                return True
        return False

def logIn(userData, JSONpath):
    with open(JSONpath, "r") as jsonFile:
        jsonData = json.load(jsonFile)
        for user in jsonData:
            if user.get("username") == userData.get("username"):
                if user.get("password") == userData.get("password"):
                    return True
        return False

def saveUser(userData, JSONpath):
    try:
        with open(JSONpath, "r") as jsonFile:
            jsonData = json.load(jsonFile)
    except json.JSONDecodeError:
        jsonData = []
    jsonData.append(userData)

    with open(JSONpath, "w") as jsonFile:
        json.dump(jsonData, jsonFile, indent= 3)



# python3 user.py
