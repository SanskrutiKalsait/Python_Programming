
#Create a Book class with title and author. Add a method display() to show book details


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)

s1 = Book("Ramayan" , "Maharishi Valmik")

s1.display()

        