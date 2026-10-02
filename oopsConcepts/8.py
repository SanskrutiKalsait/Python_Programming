
#Inheritance: Create a Vehicle class with a start() method. Create Car and Bike classes that inherit from Vehicle.

class Vehicle:
    def start(self):
        print("Vehicle started")


class Car(Vehicle):
    pass


class Bike(Vehicle):
    pass


car = Car()
bike = Bike()

car.start()
bike.start()