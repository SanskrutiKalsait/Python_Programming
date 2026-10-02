#Abstraction: Create an abstract class Employee with an abstract method calculate_salary().
#  Create a FullTimeEmployee class that implements it.

from abc import ABC, abstractmethod


class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):

    def calculate_salary(self):
        salary = 30000
        print("Salary:", salary)


e1 = FullTimeEmployee()
e1.calculate_salary()