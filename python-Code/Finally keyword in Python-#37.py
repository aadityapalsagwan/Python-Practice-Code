# Finally keyword in Python

def fun():
    try:
        l = [1, 5, 6, 3, 4]
        i = int(input("enter the index: "))
        print(l[i])
        return  1
    except:
        print("Some error occured")
        return 0

    finally:
        print("Code is successfully run")

    # print("Code is successfully run")
x  = fun()
print(x)