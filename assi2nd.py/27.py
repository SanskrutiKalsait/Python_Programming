
#Create a Student Result System using marks of 5 subjects. Calculate total, percentage, and grade using conditional statements.
m1 = 67
m2 = 90
m3 = 98
m4 = 78
m5 = 90

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("Total:", total)
print("Percentage:", percentage, "%")

if percentage >= 90:
    print("Grade A")
elif percentage >= 75:
    print("Grade B")
elif percentage >= 50:
    print("Grade C")
else:
    print("Grade D")