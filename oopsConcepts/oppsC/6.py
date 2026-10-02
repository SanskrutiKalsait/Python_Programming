
#.Create a Temperature class with a static method to convert Celsius to Fahrenheit.
class Temperature:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32

print("Temperature in Fahrenheit:", Temperature.celsius_to_fahrenheit(25))