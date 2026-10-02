#Write a simple calculator using try-except to handle invalid input and division by zero.

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("result", a*b)

except ValueError:
    print("Invalid input")

except ZeroDivisionError:
    print("Cannot divide by zero")

    