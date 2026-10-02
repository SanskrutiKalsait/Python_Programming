
#Count the total number of characters in a file.
file = open("file.txt","r")
data= file.read()
count = len(data)
print("Total number of characters:", count)
file.close()