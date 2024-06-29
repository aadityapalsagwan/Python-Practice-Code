# Generators in Python.......

def My_gen():
    for i in range(200):
        yield i # return the generator

gen = My_gen()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for j in gen:
    print(j)