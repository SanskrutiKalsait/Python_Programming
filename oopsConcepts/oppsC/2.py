#Create a Number class with a static method is_even(n) to check whether a number is even or odd.


class number:
    @staticmethod
    def is_even(n):
        if n % 2 == 0:
            print("even")

        else:
            print("odd")

number.is_even(8)

