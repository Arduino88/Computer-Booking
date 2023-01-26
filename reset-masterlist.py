import json

teachers = { #Create a dictionary and fill it with empty sub-dictionaries for each teacher
    "Mr. Jensen": {},
    "Mr. Beekers": {},
    "Mr. Kivari": {},
    "Ms. Wraight": {},
    "Ms. Best": {},
    "Mr. White": {},
    "Mr. Barraball": {},
}

with open("masterlist.json", "w") as fp: #Open masterlist.json
    json.dump(teachers, fp, indent=4, sort_keys=True) #Overwrite the contents of masterlist.json with the alphabetized pretty printed contents of the teachers dictionary with an indent of 4