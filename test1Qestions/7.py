
#7
a = 90
b = 98
c = 89
d = 90
e = 92
total = (a+b+c+d+e)
per = total/5
print(total)
print(per)
if per>=90:
    print("grade A")
elif per>=75:
    print("grade b")
elif per>=60:
    print("grade c")
elif per>=40:
    print("grade d")
else:
    print("fail")