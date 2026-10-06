# 1 Create Dog and Cat classes. Both should have a sound() method, but return different sounds

# class Dog:
#     def sound(self):
#         print("Dog says: bark")


# class Cat:
#     def sound(self):
#         print("Cat says: Meow")


# d = Dog()
# c = Cat()

# d.sound()
# c.sound()

# # 2 Create Car and Bike classes. Both should have a start() method with different outputs.

class car:
    def start(self):
        print("bike is start")

class bike:
    def start(self):
        print("car is start")

c = car()
b = bike()
c.start()
b.start()

# 3 Create Rectangle and Circle classes with an area() method. Calculate the area differently for each class

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width


# class Circle:
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius


# r = Rectangle(10, 5)
# c = Circle(7)

# print("Rectangle Area:", r.area())
# print("Circle Area:", c.area())


# # 4  Create Teacher and Student classes. Both should have a role() method with different outputs.

# class teacher:
#     def role1(self):
#         print("teaching")
# class student:
#     def role2(self):
#         print("study")

# c = teacher()
# s = student()
# c.role1()
# s.role2()


# # 5  Create Payment classes such as CashPayment and UPIPayment. Both should have a pay() method with different implementations.
# class cashPayment:
#     def pay(self):
#         print("Payment made by Cash")


# class UPIPayment:
#     def pay(self):
#         print("Payment made by UPI")


# cash = cashPayment()
# upi = UPIPayment()

# cash.pay()
# upi.pay()