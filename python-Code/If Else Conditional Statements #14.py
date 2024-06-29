# if-else statement...
'''
a = int(input("Enter your age: "))
print("Your age is: ",a)
if(a>18):
    print("Gadi lakr nikal ba ")
else:
    print("haath mt lagna gadi ko age nhi hai chalana ki.")
'''

# if-elif  statement...

'''
num = int(input("Enter the Num value is: "))
if(num < 0):
    print("-ive Value.")
elif(num == 0):
    print("num is Zero.")
else:
    print(" +ive Value.")
'''

# nested if-else statement...

num = int(input("Enter the num: "))
if(num < 0):
    print("-ive Age Value.")
elif(num > 0 ):
    if(num <= 10):
        print("Abi tu bacha hai abi teri age 10 k nicha hai")
    elif(num > 10 and num <= 20 ):
        print("Abi  bs teri age 20 ya 20 sa nicha hai")
    else:
        print("Ab tu bada hogaya hai you are adult.")
else:
    print("Number is zero.")