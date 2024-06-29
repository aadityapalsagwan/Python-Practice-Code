# Magic/Dunder Methods in Python......

class Employee:
    name = "Aaditya"
    def __len__(self):
        i = 0
        for c in self.name:
            i = i+1
        return  i

e = Employee()
print(e.name)
print(len(e))
