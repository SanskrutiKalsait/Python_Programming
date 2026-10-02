
#Write a program to take an integer from the user and handle ValueError.

try:
    a = int(input("enter 1st num"))
    b = int (input("enter 2nd num"))
except ValueError:
    print("please enter your value")