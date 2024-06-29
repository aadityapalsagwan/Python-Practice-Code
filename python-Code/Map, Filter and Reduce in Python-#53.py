# Map, Filter and Reduce in Python......
def cube(x):
    return x*x*x

'''

# map method...

l = [1,2,5,3,4]

newl = list(map(cube,l))
print(newl)

tis is a long method ...to solve the question....
newl =[]

for item in l:
    newl.append(cube(item))
'''


# Filter.............

'''
def filter_fun(a):
    return a>4

l = [1,2,5,3,4]
newli = list(filter(filter_fun, l))
print(newli)
'''

# reduce Method......

from functools import  reduce

num = [1,2,3,4,5]   # list no.
sum = reduce(lambda x,y: x+y,num)  # calculate the sum using reduce method....
print(sum)

