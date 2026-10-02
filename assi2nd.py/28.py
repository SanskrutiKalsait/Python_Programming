
#Create a Bank Withdrawal System. Take balance and withdrawal amount and check:
#Sufficient balance
#Minimum balance condition
#Invalid withdrawal amount

balance = 1000
withdraw = 1000

minimum_balance = 1000

if withdraw <= 0:
    print("Invalid withdrawal amount")
elif withdraw > balance:
    print("Insufficient balance")
elif balance - withdraw < minimum_balance:
    print("Minimum balance condition not satisfied")
else:
    balance = balance - withdraw
    print("Withdrawal successful")
    print("Remaining balance:", balance)