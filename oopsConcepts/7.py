
#Encapsulation: Create a Password class where the password is stored using a private variable.
#  Add a method to display whether the password is correct

class Password:
    def __init__(self, password):
        self.__password = password

    def check_password(self, password):
        if password == self.__password:
            print("Password is correct")
        else:
            print("Password is incorrect")


p1 = Password("12345")

p1.check_password("12345")