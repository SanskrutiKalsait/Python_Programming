
# Read and display the contents of a text file.

file = open("file.txt", "r")

content = file.read()
print(content)

file.close()