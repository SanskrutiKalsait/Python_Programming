#Display the names of all students from the JSON file.

import json

with open("student.json", "r") as file:
    students = json.load(file)

for student in students:
    print(student["name"])