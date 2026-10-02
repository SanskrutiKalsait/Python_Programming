
#Read only the first line from a file.

with open("file.txt", "r") as file:
    line = file.readline()
    print(line)

