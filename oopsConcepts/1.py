
#Create a Mobile class with brand and price. Create two objects and display their details.

class mobile:
    def __init__(self, brand , price):
        self.brand = brand
        self.price = price

    def display(self):
        print("brand =" , self.brand)
        print("price =" , self.price)
        

s1 = mobile("apple" , 150000)
s2 = mobile("samsung" , 25000)


s1.display()
s2.display()














