#Read and display the data from the JSON file.
import json

with open("student.json", "r") as file:
    students = json.load(file)

print(students)