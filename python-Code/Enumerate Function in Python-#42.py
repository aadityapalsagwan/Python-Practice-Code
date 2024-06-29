# Enumerate Function in Python

marks = [32,45,63,98,45,87,36,1,23]
# index = 0

# this is a simple method....
# for mark in marks:
#     print(mark)
#     if(index == 3):
#         print("Aditya Pal ,You are awsome!")
#     index = index+1


# this is enumerate function can make a easy ....

for index, mark in enumerate(marks):
    print(mark)
    if(index == 3):
        print("Aditya Pal,You are awaome!")
