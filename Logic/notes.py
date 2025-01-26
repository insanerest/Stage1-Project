import json

def saveNote(noteName, note, username, JSONpath):
    try:
        with open(JSONpath, "r") as jsonFile:
            jsonData = json.load(jsonFile)
            for user in jsonData:
                if user.get("username") == username:
                    if not "notes" in user:
                        user["notes"] = {}
                    user["notes"][noteName] = note
        with open(JSONpath, "w") as jsonFile:
            json.dump(jsonData, jsonFile, indent= 3)
    except (json.JSONDecodeError, KeyError) as e:

         return False
    else:
        return True
        

def getNote(noteName, username, JSONpath):
    try:
        with open(JSONpath, "r") as jsonFile:
            jsonData = json.load(jsonFile)
            for user in jsonData:
                if user.get("username") == username:
                    if "notes" in user:
                        if user["notes"][noteName]:
                            return user["notes"][noteName]
                    else:
                         user["notes"] =  {}
    except (json.JSONDecodeError, KeyError):
         return False
    else:
        return True
                        
def getAllNotes(username, JSONpath):
    try:
        with open(JSONpath, "r") as jsonFile:
            jsonData = json.load(jsonFile)
            for user in jsonData:
                if user.get("username") == username:
                     if "notes" in user:
                          return user["notes"]
                     else:
                         return {}
    except (json.JSONDecodeError, KeyError):
         return False
    else:
        return True
    
saveNote("new1", "this is the note number 1", "abd123", "./data.json")
saveNote("new2", "this is the note number 2", "abd123", "./data.json")
saveNote("new3", "this is the note number 3", "abd123", "./data.json")
print(getNote("new2", "abd123", "./data.json"))
print(getAllNotes("abd123", "./data.json"))
# python3 notes.py