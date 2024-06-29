x = 4  # global variable
print(x)
def hello():
    global x # import kr diya global x ko function mai...
    x = 6   # local variable
    print(f'The local value of x is: {x}')
    print("HEllo, Aditya Pal")

hello()
print(f'The global value of x is: {x}')
print(f'The global value of x is: {x}')
