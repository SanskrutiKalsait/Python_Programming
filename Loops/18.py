

#18. Write a program to count how many even and odd digits are present in a number.

num = 57382463906

even = 0
odd = 0
while num > 0:
    digit = num % 10

    if digit % 2 == 0:
        even += 1
    else:
        odd += 1

    num //= 10

print("Even digits:", even)
print("Odd digits:", odd)