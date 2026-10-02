
#Create a Circle class with radius. Add a method to calculate the area of the circle.

import math
class circle:
    def __init__(self , radius):
        self.radius = radius

    def area(self):
        print("area :", 3,14*self.radius*self.radius)

area_of_radius = circle(5)
area_of_radius.area()

