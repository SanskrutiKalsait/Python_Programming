
# Simple EMI Calculator
P = float(input("Enter Loan Amount: "))
R = float(input("Enter Annual Interest Rate (%): "))
T = int(input("Enter Loan Tenure (Years): "))

r = R / (12 * 100)     
n = T * 12             
EMI = (P * r * (1 + r) ** n) / ((1 + r) ** n - 1)
print("Monthly EMI =", EMI)