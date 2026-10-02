
# Q10 - convet senconds into hours,min,and seconds
total_seconds = int(input("Enter seconds: "))
hours = total_seconds /3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds / 60
seconds = remaining_seconds % 60
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)
print("_______________")