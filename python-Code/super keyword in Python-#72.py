'''
class ParentClass:
    def parent_method(self):
        print("This is the parent method.1")

class ChildClass(ParentClass):
    def parent_method(self):
        print("Adi")
        super().parent_method()



    def child_method(self):
        print("This is the child method.2")
        super().parent_method()

c1 = ChildClass()
c1.child_method()
c1.parent_method()
'''



class Employee:
  def __init__(self, name, id):
    self.name = name
    self.id = id

class Programmer(Employee):
  def __init__(self, name, id, lang):
    super().__init__( name, id)
    self.lang = lang

rohan = Employee("Rohan Das", "420")
harry = Programmer("Harry", "2345", "Python")
print(harry.name)
print(harry.id)
print(harry.lang)