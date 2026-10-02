
try:
    num = int(input("enter number"))
    print("you entered ",num)

except:
    print("invalid error")



try:
    num = int(input("enter 1st value"))
    num = int(input("enter 2st value"))

    print("result", num/num)

except ZeroDivisionError:
    print("can not divide by zero")

except ValueError:
    print("please enter number only")

    

try:
    name = input("enter your name ")
    print("your name is :" , name)
    age = int(input("enter your age "))
    print("your age is :" , age)

except ValueError:
    print("pleas enter your value")


try:
    a = 10/0
except ZeroDivisionError:
    print("can not divided by zero")

finally:
    print("program end")



