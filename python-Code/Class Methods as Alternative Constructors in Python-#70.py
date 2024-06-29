# Class Methods as Alternative Constructors in Python .........


class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromstr(cls,str):
        return cls (str.split("-")[0],str.split("-")[1],)   # ya string ko list ma convert kerta hai....

e = Employee("Adi",12000)
print(e.name)
print(e.salary)

str = "Aditya-12"
e = Employee.fromstr(str)
print(e.name)
print(e.salary)