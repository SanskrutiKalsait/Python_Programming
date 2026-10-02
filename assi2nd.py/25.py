
#Take a number and check whether it is a 3-digit number, 2-digit number, 1-digit number, or more than 3 digits.
num = 567

if num >= 100 and num <= 999:
    print("3-digit number")
elif num >= 10 and num <= 99:
    print("2-digit number")
elif num >= 0 and num <= 9:
    print("1-digit number")
else:
    print("More than 3 digits")