
#Copy the contents of one file into another file.
with open("file.txt", "r") as file1:
    data = file1.read()

with open("file2.txt", "w") as file2:
    file2.write(data)

print("File copied successfully.")