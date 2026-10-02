
#Write a program to open a file. Handle FileNotFoundError.

try:
    file = open("tyyt.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("this file is not found")

