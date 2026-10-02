#Create a simple ATM condition: balance ≥ withdrawal amount and withdrawal amount > 0.
balance = 67890
withdraw = 34457

if balance >= withdraw and withdraw > 0:
    print("Withdrawal successful.")
else:
    print("Withdrawal failed.")

