#Write a program to convert user input into an integer. Display "Invalid number" if an error occurs.

try:
    a = int(input("enter value"))
    print("number", a)

except ValueError:
    print("this is invalid number")