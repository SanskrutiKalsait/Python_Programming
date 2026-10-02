#Add a new student record to the JSON file.
import json

with open("josnfile.json", "r") as file:
    students = json.load(file)

new_student = {"id": 6, "name": "Neha", "marks": 88}
students.append(new_student)

with open("student.json", "w") as file:
    json.dump(students, file, indent=4)

print("New student added")