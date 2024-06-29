# Decorators in Python .....

def greet(fx):
    def mfx():
        print("Hello Aditya Sir")
        fx()
        print("Thanks aditya sir for using this function")
    return mfx
@greet
def hello():
    print("Hello World!")

def add(a,b):
   print(a+b)

hello()
add(5,8)
