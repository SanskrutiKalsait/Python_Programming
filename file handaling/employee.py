import json
with open("employee.json", "r") as file:
    data = json.load(file)
    print(data)
    
for employee in data:
    print(employee["name"])
    print(employee["age"])
    print(employee["city"])