# seek(), tell() and other functions....

'''
with open('adi.txt','r') as f:
     print(type(f))
     f.seek(10)   # move to thte 10th byte in the file....

     print(f.tell())  # ya bata hai ki seek ki value kha tak hai....
     data = f.read(5)  # read the next 5 bytes
     print(data)
'''

with open('adi.txt','w') as f:
     f.write("Hello, Aditya")
     f.truncate(5)  # bolta ki bs 5 he value likhe jeygi file mai...

with open('adi.txt','r') as f:
     print(f.read())

