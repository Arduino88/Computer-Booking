import json

teachers = {
    "Mr. Jensen": {},
    "Mr. Beekers": {},
    "Mr. Kivari": {},
    "Ms. Wraight": {},
    "Ms. Best": {},
    "Mr. White": {},
    "Mr. Barraball": {},
}

with open("masterlist.json", "w") as fp:
    json.dump(teachers, fp, indent=4, sort_keys=True)