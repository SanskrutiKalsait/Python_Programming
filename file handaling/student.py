import csv
with open("datastudent.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
