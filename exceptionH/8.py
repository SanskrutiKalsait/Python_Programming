#Write a program that handles both ValueError and ZeroDivisionError.

try:
    a = 10/0
except ZeroDivisionError:
    print("cannot divide into zero")
except ValueError:
    print("please enter a value")
finally:
    print("end program")