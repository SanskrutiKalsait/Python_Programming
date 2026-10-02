
#16. Write a program to find the largest digit in a number.
num = 569432

largest = 0

while num > 0:
    digit = num % 10
    if digit > largest:
        largest = digit
    num //= 10

print("Largest digit:", largest)