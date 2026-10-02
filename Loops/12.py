
#Write a program to count the number of digits in a number using a loop.
n = 12345

count = 0

while n > 0:
    n = n // 10
    count += 1

print("Number of digits =", count)