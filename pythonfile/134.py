
#for loop
for i in range(11):
    print(i)

print("______________")

#while loop
count = 1
while count<=5:
    print(count)
    count+=1

    
print("______________")


#break
for i in range(1,6):
    if i ==5:
        break
    print(i)
    
print("______________")

#continue
for i in range(1,6):
    if i==4:
        continue
    print(i)

    
print("______________")

#pass
for i in range(1,5):
    pass

print("______________")

#nested loop
for i in range(5):
    for a in range(6):
        print("*",end =" ")
    print()

print("______________")

for i in range(1,7):
    for a in range(1,5):
        print("*",end =" ")
    print()




