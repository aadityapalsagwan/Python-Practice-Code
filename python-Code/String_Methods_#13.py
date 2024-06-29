# string are immutable
'''
a = "Aditya Pal"
print(a)
print(len(a))

print(a.upper())
print(a.lower())
'''

b = "Adi !!!"
print(b.rstrip("!"))  #ya last k !! mark ko remove kerta hai or ya start mai remove nhi hota..
print(b.replace("Adi","Aaditya"))  # ya original position pa name ko change kereta hai..
print(b.split(" ")) # ya alag kerta hai with " , " the help of this..

c = "hello Aditya "
print(c.capitalize()) # starting k letter ko capital krta hai..

str1 = "Welcome to my Channel.."
print(len(str1))
print(str1.center(50))  # 50 ka button ka space deta hai..
print(len(str1.center(50)))  # or ya total length bata hai str1 ki is 50 because 50 is wnd point..


print(b.count("Adi"))  # ya bata hai ki b string kitni jega or use hui or uske ander likha hua kitna bar repeat hua hua hai

print(b.endswith("!!!"))  # bata hai ki " !!! " marks sa end hua hai ya nhi or ya reslut boolean mai deta hai true or false..

str2 = "My name's Aditya and your name is Rohan."
print(str2.find("is"))  # bata hai ki is kha pr use hua hai.. or ya position be bata hai

str3 = "CodeWithHarry"
print(str3.isalnum(),"Yes Done")  # bata hai ki sab character start with capital or attatch hai kya

str4 = "Welcome00"
print(str4.isalpha()," Done")

str5 = "   "
print(str5.isspace()) # space bata hai..
