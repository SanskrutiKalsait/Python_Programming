#Take three sides and check whether a triangle is valid or not.
a = 36
b = 34
c = 67

if a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")
else:
    print("Not a Valid Triangle")