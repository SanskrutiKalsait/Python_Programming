
#.Create a Calculator class with a static method add(a, b) to add two numbers

class Calculator:
    @staticmethod
    def add(a,b):
        return a+b

add = Calculator.add(20, 47)
print("Addition =", add)