# Inheritance in Python......

class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"The name of Employee: {self.name} and the id is: {self.id}")


class Programmer(Employee):   #inheritance......
    def showlanguage(self):
        print("The default Language is Python.")
        print(f"The name of Employee: {self.name} and the id is: {self.id}")




e = Employee("Aditya Pal",1001)
e.showDetails()
e = Programmer("Parth",1002)
e.showDetails()

