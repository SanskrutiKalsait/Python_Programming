#Read and display all records from the CSV file.
import csv
with open("cvsfile.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)