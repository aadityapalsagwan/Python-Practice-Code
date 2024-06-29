# Function Caching in Python.......

import functools
import time

@functools.lru_cache(maxsize=None)
def fx(n):
    time.sleep(5)
    return n*5
print(fx(20))
print("Done For 20")
print(fx(2))
print("Done For 2")
print(fx(6))
print("Done For 6")

print("Ab fir dubaara sa.......")

print(fx(20))
print("Done For 20")
print(fx(2))
print("Done For 2")
print(fx(6))
print("Done For 6")