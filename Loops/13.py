
#Write a program to find the sum of digits of a number.
n = 123456

sum = 0

while n > 0:
    digit = n % 10
    sum += digit
    n = n // 10

print("Sum of digits =", sum)