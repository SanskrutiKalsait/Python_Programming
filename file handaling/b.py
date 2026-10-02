
#reading
file = open("text.txt","r")
data = file.read
print(data)
file.close()
 
#reading
file = open("text.txt", "w")
file.write("hello i am sanskruti\ni am from latur")
file.close()


#append
file = open("text.txt","a")
file.write("\nmy education in diploma")
file.close()