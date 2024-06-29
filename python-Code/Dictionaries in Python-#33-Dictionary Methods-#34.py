'''
dic = {
    "Adi":"Human Being",
    "Spoon":"Object"
}
print(dic["Adi"])

info = {'Name':'Aditya','Age':'20'}
print(info) # sub print hojeyga...
print(info.keys()) # key print hojeygi eg: name , age..
for key in info.keys():
    print(info[key]) # keys ki value print hojeygi eg: adi ,20..
    print(f'The value corresponding to the key{key} is {info[key]}')
'''



# Dictionary Methods......

ep1 = {12:1 , 13:2 , 14:3 , 15:4}
ep2 = {13:23 , 16:34 , 17:45 , 18:56 , 19:78}
# ep1.update(ep2)
# ep1.clear()
# ep1.pop(12)
ep1.popitem() # last item delete
print(ep1)