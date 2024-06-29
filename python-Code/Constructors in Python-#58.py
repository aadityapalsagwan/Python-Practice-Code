# Constructors in Python......

class person:
    name = ""
    occ = ""

    def __init__(self,n,o):   # create a constructor...
        print("Hello Aditya Sir.")
        self.name = n
        self.occ = o

    def info(self):
        print(f'{self.name} is a {self.occ}')

a = person("Aditya","Web-developer")
b = person("Dubey","Web-developer")



# a.name ="Aditya Pal"
# a.occ = "Web-developer"
a.info()
b.info()