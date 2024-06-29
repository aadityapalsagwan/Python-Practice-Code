'''
tup = (1,5,9)
# tup[0]= 45 # tuple ko hum change nhi kr skta hai..
print(type(tup))
print(tup)
'''


# Operations on Tuples..

country = ("India","Sri Lanka","China","PK")
temp = list(country)
temp.append("Russia")   # add item in country tuple
temp.pop(3)            # remove item in tuple country
temp[2]= "Finland"      # change item
country = tuple(temp)
print(country)

