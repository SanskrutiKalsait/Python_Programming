#Create a student.json file and store details of 5 students.
import json
students = [
    {"ID": 1, "Name": "Amit", "Marks": 85},
    {"ID": 2, "Name": "Sneha", "Marks": 90},
    {"ID": 3, "Name": "Rahul", "Marks": 78},
    {"ID": 4, "Name": "Priya", "Marks": 88},
    {"ID": 5, "Name": "Rohit", "Marks": 75}
]
with open("josnfile.json", "w") as file:
    json.dump(students, file, indent=4)
for student in students:
    print(student)