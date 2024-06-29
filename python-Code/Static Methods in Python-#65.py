# Static Methods in Python....

class Math:
    def __init__(self,num):
        self.num = num

    def addtonum(self,n):
        self.num = self.num + n

    @staticmethod
    def add(a,b):
        return  a+b

a = Math(5)
print(a.num)
a.addtonum(7)
print(a.num)





# result = Math.add(5,6)
# print(result)