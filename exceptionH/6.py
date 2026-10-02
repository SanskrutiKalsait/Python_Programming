
#Write a program using try-except-finally to divide two numbers.

try:
    a = 10/0
except ZeroDivisionError:
    print("cannot divide into zero")
finally:
    print("program end")
