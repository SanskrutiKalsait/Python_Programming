
# INR to USD Currency Converter
exchange_rate = 87.0

inr = float(input("Enter amount in INR: "))
usd = inr / exchange_rate

print("INR:", inr)
print("USD:", round(usd, 2))