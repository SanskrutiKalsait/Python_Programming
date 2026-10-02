
#Create a Simple Calculator.Take two numbers and an operator (+, -, *, /) and perform the operation using if-elif-else.

a = 10
b = 5
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
else:
    print("Invalid operator")