x = int(input("Enter the num: "))
match x:
    case 0:
        print("Case is 0")
    case 4:
        print("Case is 4")
    case _ if x!=90:  # ya default hota hai..
        print(x,"is not 90")
    case _ if x!=80:  # ya default hota hai..
        print(x,"is not 80")
    case _:  # ya default hota hai..
        print(x)