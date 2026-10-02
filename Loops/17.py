
#Write a program to find the smallest digit in a number.


num = 569432

smallest = 9

while num > 0:
    digit = num % 10
    if digit < smallest:
        smallest = digit
    num //= 10

print("Smallest digit:", smallest)