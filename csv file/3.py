#Add a new student record to the CSV file.
import csv
with open("cvsfile.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([6, "atharv", 88])