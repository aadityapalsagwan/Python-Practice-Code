# Class Methods in Python.....

class Employee:
    companyName = "Apple"
    def show(self):
        print(f'The Name of Own that company is {self.name} and the company name is: {self.companyName}')
    @classmethod   # company name real mai change kerta hai.....
    def changeCompany(cls,newCompany):
        cls.companyName = newCompany    # or ya method simple ho without @class,ethod to to copy banata hai or usko print kerta hai or ral mai change nhi kerta
        

e = Employee()
e.name = "Aaditya Pal"
e.show()
e.changeCompany("Tesla")
e.show()
e.changeCompany("Google")
e.show()
e.changeCompany("MicroSoft")
e.show()
e.changeCompany("Tata")
e.show()
e.changeCompany("Adani Group")
e.show()
e.changeCompany("Reliance")
e.show()

print(Employee.companyName)