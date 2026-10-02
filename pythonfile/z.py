

#parameter 
print("area of parameter =")
side = int(input("enter the side of squre"))
area = side*side
print (area)
perimeter = 4*side
print (perimeter)
print("____________________")

# calcculate per
print("calculate per =")
num1 = int(input("enter marathi marks"))
num2 = int(input("enter hindi marks"))
num3 = int(input("enter english marks"))
num4 = int(input("enter math marks"))
num5 = int(input("enter science marks"))
obtmarks = (num1+num2+num3+num4+num5)
totalmarks = 500
percentage = (obtmarks/totalmarks)*100
print ("enter obtmarks =",obtmarks)
print ("enter totalmarks =",totalmarks)
print( "total percentage=",percentage)
print("______________")

#calculate avg
print("calculate avrage =")
num1 = int(input("enter your num1"))
num2 = int(input("enter your num2"))
num3 = int(input("enter your num3"))
avg = (num1+num2+num3)/3
print("total avrage =",avg)
print("_______________")

#swaping num
a = int(input("enter 1st num"))
b = int(input("enter 2nd num"))
a , b = b , a
print( a)
print( b)

