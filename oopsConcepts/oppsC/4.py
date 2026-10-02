#Create an Employee class with a class variable company. Create a class method to change the company name.

class Employee:
    company = "Technobrillient"

    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company


print(Employee.company)

Employee.change_company("Infosys")

print(Employee.company)

        