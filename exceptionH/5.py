
#Create a dictionary with student details. Access a key that does not exist and handle KeyError.

student = {
    "name": "sanskruti",
    "age" :"19"
    
}

try:
    print(student ["marks"])
except KeyError:
    print("no exits")