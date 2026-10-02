
#Create a Person class with a method introduce(). Create a Student class that inherits from Person and add a study() method.

class Person:
    def introduce(self):
        print("Hello, I am a person")


class Student(Person):
    def study(self):
        print("I am studying Python")


s1 = Student()

s1.introduce()
s1.study()