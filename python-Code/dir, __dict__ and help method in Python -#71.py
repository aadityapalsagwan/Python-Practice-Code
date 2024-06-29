# dir, __dict__ and help method in Python.........

# x = [1,5,9]
# print(dir(x))


class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p= person("Aditya",21)
print(p.__dict__)

print(help(person))
