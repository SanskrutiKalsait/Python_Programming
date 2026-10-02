
#Append new data to an existing file and display the updated content.

file = open("file.txt", "a")
file.write("College: government polytechnic\n")
file.close()


file = open("file.txt","r")
content = file.read()
print(content)
file.close()


