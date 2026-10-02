#Create a Circle class with a static method area(radius) to calculate the area of a circle.

class Circle:
    @staticmethod
    def area(radius):
        return 3.14 * radius * radius

print("Area of circle:", Circle.area(5))