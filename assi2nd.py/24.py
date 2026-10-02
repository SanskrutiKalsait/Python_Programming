
# Take three sides and determine whether the triangle is:

#Equilateral
#Isosceles
#Scalene

a = 78
b = 34
c = 56

if a == b and b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")