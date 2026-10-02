
file = open("demo.text", "w")
file.write("hello word")
file.close()

file = open("demo.text","r")
data = file.read
print(data)
file.close()

#append
file = open("demo.text","a")
file.write("\nhello paython")
file.close()

