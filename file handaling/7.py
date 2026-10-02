
#Read a file line by line using a loop.
file = open("file.txt", "r")

for line in file:
    print(line)
file.close()