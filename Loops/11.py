
#Write a program to find the factorial of a number using a loop.
n = 5

factorial = 1

for i in range(1, n + 1):
    factorial *= i

print("Factorial =", factorial)