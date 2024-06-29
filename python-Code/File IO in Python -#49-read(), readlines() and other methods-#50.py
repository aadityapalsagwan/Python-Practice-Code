# Reading a file content.....
'''
f = open('adi.txt','r')
# print(f)
text =f.read()
print(text)
f.close()
'''

# Writing a file content....

'''
f = open('adi1.txt','a')
f.write('Hello Aditya pal\n')
# f.close()

with open('adi1.txt','a'):
    f.write("I'm inside bro!\n")
'''


# read(), readlines() and other methods.....

'''
f = open('adi.txt','r')
i = 0
while True:
    i = i+1
    line = f.readline()
    if not line:
        break

    m1 = int(line.split(",")[0])
    m2 = int(line.split(",")[1])
    m3 = int(line.split(",")[2])
    print(f"Marks of student {i} in Maths is: {m1}")
    print(f"Marks of student {i} in English is: {m2}")
    print(f"Marks of student {i} in SSt is: {m3}")

    print("\n",line)
'''

f = open('adi2.txt','w')
lines = ['line-1\n','line-2\n','line-3\n']
f.writelines(lines)
f.close()
