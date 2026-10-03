#Update the marks of a student in the JSON file.
import json

with open("student.json", "r") as file:
    data = json.load(file)

for student in data["students"]:
    if student["name"] == "Rahul":
        student["marks"] = 95

with open("student.json", "w") as file:
    json.dump(data, file, indent=4)

print("Marks updated successfully")