
#Polymorphism: Create Circle and Rectangle classes. Both should have an area() method, but calculate the area differently.

class Circle:
    def area(self):
        radius = 5
        return 3.14 * radius * radius


class Rectangle:
    def area(self):
        length = 10
        width = 5
        return length * width


c = Circle()
r = Rectangle()

print("Circle Area:", c.area())
print("Rectangle Area:", r.area())