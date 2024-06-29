# Time Module in Python ..................

import time

'''
def usingWhile():
    i = 0
    while i <100:
        i= i+1
        print(i)
def usingFor():
    for i in range(100):
        print(i)
init = time.time()
usingFor()
print(time.time() - init)
init = time.time()
usingWhile()
print(time.time() - init)
'''

t = time.localtime()
formatted_time =time.strftime("%y-%m-%d %H:%M:%S",t)
print(formatted_time)

