
#Create a Movie Ticket System.
#Take age and calculate ticket category:
#Below 5 → Free
#5–12 → Child Ticket
#13–59 → Regular Ticket
#60+ → Senior Citizen Ticket

age = 45

if age < 5:
    print("Free")
elif age <= 12:
    print("Child Ticket")
elif age <= 59:
    print("Regular Ticket")
else:
    print("Senior Citizen Ticket")
