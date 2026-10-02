
#Write a program to take two numbers from the user and perform addition. Handle invalid input.

try:
    a = int(input("enter 1st value"))
    b = int(input("enter 2nd value"))
   
    result = a + b
    print("result",result)

except ValueError:
    print("Invalid input Please enter only numbers ")
