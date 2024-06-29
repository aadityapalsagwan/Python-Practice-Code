
def average(a,b):
    print("The average number is: ",(a+b)/2)
def avg(*num):
    print(type(num))
    sum = 0
    for i in num:
        sum = sum +i
    print(" Average is: ",sum/len(num))

# average(4,9)
avg(5 , 4 ,5,4,6,8)
