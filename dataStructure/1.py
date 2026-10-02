
#Create a variable containing your name. Print your name, its length, uppercase, and lowercase form.
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius


# Create object
c = Circle(5)

# Display area
print("Area of circle:", c.area())