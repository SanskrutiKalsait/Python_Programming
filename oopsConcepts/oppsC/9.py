#Create a Math class with static methods for addition, subtraction, multiplication, and division.

class Math:
    
    @staticmethod
    def addition(a, b):
        return a + b

    @staticmethod
    def subtraction(a, b):
        return a - b

    @staticmethod
    def multiplication(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        return a / b


print("Addition:", Math.addition(10, 5))
print("Subtraction:", Math.subtraction(10, 5))
print("Multiplication:", Math.multiplication(10, 5))
print("Division:", Math.division(10, 5))