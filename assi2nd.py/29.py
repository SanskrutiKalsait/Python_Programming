
#Take a month number (1–12) and display the month name and number of days.
month = 11

months = {
    1: ("January", 31),
    2: ("February", 28),
    3: ("March", 31),
    4: ("April", 30),
    5: ("May", 31),
    6: ("June", 30),
    7: ("July", 31),
    8: ("August", 31),
    9: ("September", 30),
    10: ("October", 31),
    11: ("November", 30),
    12: ("December", 31)
}

if month in months:
    name, days = months[month]
    print(name, "has", days, "days.")
else:
    print("Invalid month number!")