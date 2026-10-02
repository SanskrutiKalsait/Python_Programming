
#Create a list [10, 20, 30]. Ask the user for an index and handle IndexError.

numbers =[ 10,20,30]
try:
    index = int(input("enter index :"))
    print("value:", numbers[index])

except IndexError:
    print("index error")
except ValueError:
    print("enter only value")

