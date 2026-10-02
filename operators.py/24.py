
# Create a Bank Balance Program.
# Initial Balance = ₹5000
# Deposit Amount
# Withdraw Amount
# Display Final Balance

balance = 5000
print("initial balance = 5000")

deposit = int(input("Enter deposit"))
withdraw = int(input("Enter withdraw"))

balance += deposit
balance -= withdraw

print("Final Balance:", balance)