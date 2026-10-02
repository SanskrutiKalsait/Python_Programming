
#Create an Online Shopping Cart with Discount.

item = input("Enter Item Name: ")
price = int(input("Enter Item Price: "))
quantity = int(input("Enter Quantity: "))

total = price * quantity
discount = total * 10 / 100
final = total - discount

print("Item:", item)
print("Total Amount:", total)
print("Discount (10%):", discount)
print("Final Amount:", final)