
# Q12 - create an employee salary calculate (baisc ,HRA, DA ,gross salary)
basic_s = float(input("Enter basic salary"))
hra = basic_s * 20/100
da = basic_s * 10/100
gross_s = basic_s + hra+ da
print (" basic salary :",basic_s)
print ("HRA :",hra)
print ("DA :",da)
print ("gross salary :",gross_s)
print("______________")