# Access Modifiers in Python.......

class Employee:
    def __init__(self):
        self.name = "Aditya"
        self.__name1 = "Adi"  # this is a private modifier....
        self.id = 1001

a = Employee()
print(a.name)   # this is a public modifier..
print(a.id)
print(a._Employee__name1)   #  this is a private modifier can easy access.....
