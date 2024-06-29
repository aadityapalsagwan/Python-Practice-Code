# this is a simple list code...

'''
l = [2,6,5]
print(l)
print(type(l))
print(l[0])
print(l[1])
print(l[2])
print(l[-1],"-ive index") # -ive index
print(l[len(l)-2])  # convert -ive to +ive index

if "Adi" in l:
    print("Yes name is here..")
else:
    print("Name is not here..")

if 2 in l:
    print("Yes num is here")
else:
    print("Num is not here..")
'''

# list Comprehension
'''
lst = [i*i for i in range(5)]
print(lst)
'''

# ....................... List Methods Start.........................

l = [45,85,96,1,5,8,1,5,1]
'''
 print(l," Done")
 l.append(100) # append add keta hai vaue ko kisi bi list ya anyWhere...
 l.sort()  # ascending order.....
 l.sort(reverse = True) # descending order.....
 l.reverse()  # reverse kerti hai....
 print(l)
 print(l.index(1),"hogaya")
 print(l.count(1),"Ab khatam")
'''


# ya original list mai change kerta hai...
'''
# m = l.copy()
m = l
m[0] = 9
l.insert(1, 0)  # ya list mai koi bi position pa value ko change kerta hai..
'''
'''
ya method list ko extend kerna mai or usmai value ko add kerna mai ata hai...

m =[200,300,400]
k= l+m
print(k) # issa bi merge hojati hai list..
l.extend(m)
'''

print(l)

