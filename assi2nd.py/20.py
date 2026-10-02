
#: Create a Shopping Discount System:

#Purchase ≥ ₹5000 → 20% discount
#Purchase ≥ ₹3000 → 15% discount
#Purchase ≥ ₹1000 → 10% discount
#Below ₹1000 → No discount

purchase = 56789
if purchase >= 5000:
    print("20% discount")
elif purchase >= 3000:
    print("15% discount")
elif purchase >= 1000:
    print("10% discount")
else:
    print("No discount")