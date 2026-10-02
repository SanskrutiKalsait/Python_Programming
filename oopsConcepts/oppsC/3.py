#Create a Student class with a class variable school. Create a class method to display the school name.

class student:
    school = "dnyaneshwar school"
    @classmethod
    def display_school(cls):
        print ("School name :", cls.school)
        
student.display_school()