
# Restaurant Billing System
item1 = input("Enter Item 1: ")
price1 = float(input("Enter Price 1: "))

item2 = input("Enter Item 2: ")
price2 = float(input("Enter Price 2: "))


total = price1 + price2 
gst = total * 0.05     
bill = total + gst
print(item1, ":", price1)
print(item2, ":", price2)
print("Total Amount :", total)
print("GST (5%)     :", gst)
print("Final Bill   :", bill)