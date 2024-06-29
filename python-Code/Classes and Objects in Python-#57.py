# Classes and Objects in Python......

class person:
    name = "Aditya"
    occupation = "Developer"
    networth = 2

    def info(self):
        print(f'{self.name} is a {self.occupation} and the networth is {self.networth} Billion.')

a =person()  # object of class....
a.info()

# a.name = "Dubey"
# print(a.name)
# print(a.occupation)
# print(a.networth)