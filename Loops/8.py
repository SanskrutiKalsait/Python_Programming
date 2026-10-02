
#Write a program to calculate the sum of all even numbers from 1 to N.
N = 10

total = 0
for i in range(2, N + 1, 2):
    total += i

print("Sum of even numbers =", total)