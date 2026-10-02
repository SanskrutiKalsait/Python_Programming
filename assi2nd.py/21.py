
#Create an Electricity Bill Calculator based on units consumed:

#Up to 100 units → ₹5/unit
#101–200 → ₹7/unit
#Above 200 → ₹10/unit

units = 567

if units <= 100:
    bill = units * 5
    print("Electricity Bill: ₹", bill)

elif units <= 200:
    bill = units * 7
    print("Electricity Bill: ₹", bill)

else:
    bill = units * 10
    print("Electricity Bill: ₹", bill)

