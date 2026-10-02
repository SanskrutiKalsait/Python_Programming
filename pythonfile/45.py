
# #IF ELSE
# #1
num = 4
if num %2 ==0 :
    print("even")
else:
     ("odd")


#2
num = 5
if num >=0:
     print("positive")
else:
     print("negative")


# fruit =["banna","mango","apple","orange"]
# print(fruit.append("kiwi"))
# print(fruit.insert(1,"watermelen"))
# last = fruit.pop()
# print(last)
# print(fruit)

# def fruit():
#     fruit =["mango", "apple","apple", "orange"]
#     fruit.append("kiwi")
#     print(fruit)
#     fruit.insert(1,"watermelen")
#     print(fruit)
#     last = fruit.pop()
#     print(last)
#     print(fruit)
#     print(fruit.count("apple"))
#     fruit.reverse()
#     print(fruit)
    

# fruit()


#oops

# class Democlass():
#     def __init__(self,name,age):
#         self.name= name
#         self.age = age

# # s1 = Democlass("sanskruti","19")
# # print(s1.name,s1.age)

# # #encapculation
# # class D():
# #     def __init__(self, balance):
# #         self._balancebalance = balance

# obj=D()
# print(D.balance)


# class D():
#     def set_balance (self, balance):
#         self.__balance = balance

#     def getbalance(self):
#         return self.__balance

# obj = D()
# obj.set_balance(2000)
# bal =obj.getbalance()
# print(bal)


# class D():
#     def set_balance(self,balance):
#         self.balance = balance
        
# class D1(D):
#     def getbalance(self):
#        return self.balance

# obj =D1()
# obj.set_balance(200000)

# ob= obj.getbalance()
# print(ob)

# class parent():
#     def display(self):
#         print("father")

# class parent2():
#     print("mother")

# class son(parent,parent2):
#     def display(self):
#         print("son")

# obj = son()
# obj.display()


# class Gfather():
#     def display(self):
#         print("Gfather")

# class father(Gfather):
#     def display(self):
#         print("father")

# class son(father):
#     def display(self):
#         print("son")
# obj = father()
# obj.display()
# obj = son()
# obj.display()


#form input abc, abstract method and just an not theri abstract mehtod
# from abc import ABC,abstractmethod 
# class Animal():
#     @abstractmethod
#     def sound(self):
#         pass
#     def walk(self):
#         pass

# class dog(Animal):
#     def sound(self):
#         print("dog sound is bark")

#     def walk(self):
#         print("xyz")

# class cat(Animal):
#     def sound(self):
#        print("cat sound is meow")
    
#     def walk(self):
#         print("xyzyy")

# d = dog()
# c = cat()
# d.sound()
# d.walk()
# c.sound()
# c.walk()

# class A():
#     a = int(input("enter value 1st"))
#     b = int(input("enter value 2nd"))

#     try:
#         c= a/b
#         print(c)
#     except(ZeroDivisionError):
#         print("can not by divide zero")
#     finally:
#         print("end program")
# # obj= A()


# class exception():
    
#     try:
#         a = eval(input("enter value 1st"))
#         b = eval(input("enter value 2nd"))
#         c= a/b
#         print(c)
#     except(ValueError):
#         print("only use numbers")
#     except (ZeroDivisionError):
#         print("can not by divide zero")
#     except (Exception):
#         print("exception")
#     else:
#          print("program executed")
#     finally:
#         print


# obj= exception()

# try:
#     age=50
#     if age<18:
#         raise ValueError("must be 18 or above")
#     print("eligible")
# except ValueError as e:
#     print("Error",e)        




# n=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# print(n[-1])


# from abc import ABC , abstractmethod
# class star(ABC):
#     @abstractmethod
#     def display(self):
#         pass

# class pattern(star):
#     def display(self):
#      for i in range(1,6):
#             print("*"*i)

# s=pattern()
# s.display()

# print("______________________")

# from abc import ABC , abstractmethod
# class star(ABC):
#     @abstractmethod
#     def display(self):
#         pass

# class pattern(star):
#     def display(self):
#      for i in range(6,0,-1):
#             print("*"*i)

# s=pattern()
# s.display()

# print("______________________")
# from abc import ABC , abstractmethod
# class star(ABC):
#     @abstractmethod
#     def display(self):
#         pass

# class pattern(star):
#     def display(self):
#         for i in range(7,0,-1):
#             print("*"*i )

#         for i in range(1,7):
#                     print("*"*i )
    


# s=pattern()
# s.display()






