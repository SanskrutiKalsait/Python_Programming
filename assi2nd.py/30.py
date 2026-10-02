
# Create a Restaurant Billing System. Take food item choice and quantity, calculate the bill, and apply a discount based on the total amount.
food = "Pizza"
quantity = 3

if food == "Pizza":
    price = 200
elif food == "Burger":
    price = 100
elif food == "Pasta":
    price = 150

total = price * quantity

if total >= 500:
    discount = total * 10 / 100
elif total >= 300:
    discount = total * 5 / 100
else:
    discount = 0

bill = total - discount

print("Food:", food)
print("Quantity:", quantity)
print("Total:", total)
print("Discount:", discount)
print("Final Bill:", bill)
    