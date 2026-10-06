
#  1 Create a Person class with a name variable. Create a Student class that inherits from Person and print the student's name.

# class person:
#     def __init__(self ,name):
#         self.name = name

# class student(person):
#     def display(self):
#         print("student name:", self.name)

# s1 = student("sanskruti")
# s1.display()

# #  2 Create a Vehicle class with a start() method. Create a Car class that inherits from Vehicle.

# class vehical:
#     def start(self):
#         print("start vehical")
# class car(vehical):
#     pass
# c1 = car()
# c1.start()
        
# # 3 Create a Animal class with a sound() method. Create a Dog class that inherits from Animal.

# class Animal:
#     def sound(self):
#         print("animal make sound")

# class dog(Animal):
#     def sound(self):
#         print("dog spark")

# d = dog()
# d.sound()

# # 4 Create a Employee class with name and salary. Create a Manager class that inherits from Employee and add a department variable.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department


# m1 = Manager("Sanskruti", 30000, "IT")

# print("Name:", m1.name)
# print("Salary:", m1.salary)
# print("Department:", m1.department)
        
# # 5 Create a Father class with a property() method. Create a Son class that inherits from Father.

# class father:
#     def property(self):
#         print("property of father")

# class son(father):
#     pass

# s1 = son()
# s1.property()


# 6 Create a Shape class with a display() method. Create Circle and Rectangle classes that inherit from Shape.

# class shape:
#     def display(self):
#         print("this is a shape")

# class circle(shape):
#     pass
# class rectangle(shape):
#     pass

# c = circle()
# r = rectangle()
# c.display()
# r.display()

