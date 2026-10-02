
#Create a Bank Account System (Deposit, Withdraw, Balance).

balance = 1000
print("Current Balance:", balance)

deposit = int(input("Enter deposit amount: "))
balance = balance + deposit
print("Balance after deposit:", balance)

withdraw = int(input("Enter withdrawal amount: "))
balance = balance - withdraw
print("Balance after withdrawal:", balance)

print("Final Balance:", balance)