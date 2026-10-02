#Create a Product class with a static method that checks whether the given price is greater than 0.

class Product:

    @staticmethod
    def check_price(price):
        return price > 0

print(Product.check_price(100))
