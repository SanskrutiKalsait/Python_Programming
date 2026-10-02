
#Create a student.csv file and store details of 5 students (ID, Name, Marks).
import csv
with open("cvsfile.csv", "w") as file:
    writer = csv.writer(file)

    writer.writerow(["ID", "Name", "Marks"])
    writer.writerow([1, "Rahul", 75])
    writer.writerow([2, "Amit", 80])
    writer.writerow([3, "Sneha", 85])
    writer.writerow([4, "Pooja", 70])
    writer.writerow([5, "Riya", 90])