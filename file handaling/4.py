

#Count the total number of words in a file.
file = open("file.txt", "r")
data = file.read()
words = data.split()

print("Total number of words:", len(words))

file.close()