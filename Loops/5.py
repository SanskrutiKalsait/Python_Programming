
#Write a program to print the multiplication table of a number entered by the user
num = int(input("Enter a number: "))

for i in range(4, 9):
    print(num, "x", i, "=", num * i)