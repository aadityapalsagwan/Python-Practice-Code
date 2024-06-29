# Exercise 7 Solution + Shoutouts .....

import os


import os

files = os.listdir("images")
i = 1
for file in files:
    if file.endswith(".png"):
        print(file)
        os.rename(f"Python/{file}",f"Python/{i}.png")
        i = i+1
