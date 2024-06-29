a = input("Enter the num: ")
print(f'Multiplication table of {a} is ')
try:
    for i in range(1,11):
      print(f'{int(a)} x {i} = {int(a)*i}')
except Exception as e:
    print(e)  # error remove krta hai temporary...

print("Some line of code")
print("End Khatam good bye tata....")