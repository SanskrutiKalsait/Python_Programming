
#Read only the first 5 characters from a file.

with open("file.txt", "r") as file:
    data = file.read(5)
    print(data)