import time
t = time.strftime('%H:%M:%S')
hour = int(time.strftime('%H'))
hour = int(input("Enter the Hour: "))
print(hour)

if(hour >=0 and hour <12):
    print("good Morning Sir.")
elif(hour >= 12 and hour<17):
    print("Good Afernoon Sir.")
elif(hour >=17 and hour<0):
    print("Good Night Sir.")

