# # 1 Create a Student class with name and age. Display student details.

# class student:
#     def __init__(self ,name, age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(self.name,self.age)
# s1 = student("student name :", "sanskruti")
# s2 = student("student age:", "19 ")
# s1.display()
# s2.display()



# # 2 Create a Mobile class with brand and price. Create two objects.

# class mobile:
#     def __init__(self , brand , price):
#         self.brand = brand
#         self.price = price

# m1 = mobile("apple",1500000)
# m2 = mobile("redmi", 15000)

# print(m1.brand,m1.price)
# print(m2.brand,m2.price)



# # 3 Create a Book class with title and author. Add a display() method.

# class Book:
#     def __init__(self, title , author):
#         self.title = title
#         self.author = author

#     def display(self):
#         print( self.title , self.author)

# b1 = Book("mahabharat", "maharishi ved vyas")
# b1.display()



# # 4 Create a Person class and inherit it into a Student class.

# class Person:
#     def show(self):
#         print("I am a person")

# class Student(Person):
#     pass

# s = Student()
# s.show()


# # 5 Create a Vehicle class and inherit it into a Car class.

# class Vehicle :
#     def start(self):
#         print("vehical starting")

# class car(Vehicle):
#     pass
# c = car()
# c.start()


# # 6 Create a Animal class with sound() method and override it in Dog.

# class Animal:
#     def sound(self):
#         print("Animal make sound")

# class Dog (Animal):
#     def sound(self):
#         print("dog spark")
# d = Dog()
# d.sound()


# # 7 Create a Shape class and inherit it into Circle.

# class Shape:
#     def show(self):
#         print("this is a shape")

# class Circle(Shape):
#     pass
# c = Circle()
# c.show()


# # 8 Create a Employee class and inherit it into Manager.

# class Employee:
#     def show(self):
#         print("employee worker")

# class manager(Employee):
#     pass

# E = manager()
# E.show()

# # 9 Create a Student class with a class variable school.

# class Student:
#     school = "ABC School"

# print(Student.school)


# # 10 Create a class method to change the school name.
# class student:
#     school = "savitribai international"
#     @classmethod
#     def change_school(cls,name):
#         cls.school = name
# student.change_school("jijamata school")
# print(student.school)


# # 11 Create an Employee class with class variable company.

# class Employee:
#     company = "ssk"

# print(Employee.company)


# # 12 Create a class method to change the company name.

# class company:
#     company1 = "apple"
#     @classmethod
#     def change_name(cls,name):
#         cls.company1 = name

# company.change_name("microsoft")
# print(company.company1)


# 13 Create Dog, Cat, and Cow classes. Each should have a sound() method. Use one function to call sound() for all objects.

# class dog:
#     def sound(self):
#         print("dog is bark")
# class cat:
#     def sound(self):
#         print("cat is meow")
# class cow:
#     def sound(self):
#         print("cow is moo")

# d = dog()
# c = cat()
# c = cow()

# d.sound()
# c.sound()
# c.sound()

# 14 Create a Student class with a class variable school. Display the school name.

# class student:
#     school = "ABC School"


# s1 = student()
# print(s1.school)

# 15 Demonstrate multiple inheritance using Father, Mother, and Child.

# class father:
#     def father_q(self):
#         print("father is hardwarking out off home")
# class mother:
#     def mother_q(self):
#         print("mother is working in house")

# class child(father,mother):
#     def child(self):
#         print("child is depending on parents")

# c = child()
# c.father_q()
# c.mother_q()
# c.child()

# 15 Demonstrate **multilevel inheritance** using `Grandparent → Parent → Child`.  
# class grandparents:
#     def grand_parent_birth(self):
#         print("grandparent birth year is 1955")

# class parents(grandparents):
#     def parent_birth(self):
#         print("parents birth year is 1978")

# class child(parents):
#     def child_birth(self):
#         print("child bith year is 2007")

# c = child()
# c.grand_parent_birth()
# c.parent_birth()
# c.child_birth()

# 16 Demonstrate **method overriding** using `Animal`, `Dog`, and `Cat`.  
# class Animal:
#     def sound(self):
#         print("animal sound")

# class dog(Animal):
#     def sound(self):
#         print("dog sound is  bark")

# class cat(Animal):
#     def sound(self):
#         print("cat sound is meow")

# d = dog()
# c = cat()
# d.sound()
# c.sound()



# marks =[20 , 48, 25, 23]

# total = sum(marks)
# percentage = total /4

# atkt = 0

# for marks in marks:
#     if marks < 40:
#         atkt += 1

# print("total :", total)
# print("percentage :", percentage)
# print("atkt subject:", atkt)

# if percentage > 90:
#     print("A grade")

# elif percentage > 80:
#     print(" B grade")

# elif atkt == 0:
#     print("percentage :" ,percentage)

# else :
#     print("percentage : percentage is not allow to ATKT" )
#     print("fail")


# n = "NITIN"

# reverse = n

# while n > n:
#     name = n % 10
#     reverse = reverse * 10 + name
#     n = n// name
# print ("reverse =", reverse)

# str = "Techno"
# t = len(str)

# for a in range(t-1,-1,-1):
#     print(str[a])


# str ="assf"
# print(str.isalpha())

# str =" technobrilliant"
# print(str.find ("s"))

# print(str.index("s"))


# age = int (input("enter your age:"))
# sum = age + 1
# print ("next year age :", sum)


# list = [1,2,3,[4,5,6],7,[8,9,10]]
# print(list[3])

# print(list[0::2])

# class Student:
#     def __init__(self):
#         self.__age = 20

#     # Getter
#     def get_age(self):
#         return self.__age

#     # Setter
#     def set_age(self, age):
#         self.__age = age


# s = Student()

# print(s.get_age())   # Getter

# s.set_age(25)        # Setter

# print(s.get_age())



class Animal:
    def sound(self):
        print("Animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

d = Dog()
d.sound()