
#Write a program to calculate the sum of all odd numbers from 1 to N.
N = 5

total = 0

for i in range(1, N + 1, 2):
    total += i

print("Sum of odd numbers:", total)