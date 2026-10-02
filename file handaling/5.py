
#Count the total number of lines in a file.

file =open("file.txt","r")
lines = file.readlines()
print("Total number of line:",len(lines))
file.close()
