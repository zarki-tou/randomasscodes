# Import the time library
import time
mytime=int(input("enter ur time: "))
arange=int(input("range of a: "))
a=0
while a<=arange:
    print(a,end="")
    a+=1
for x in range(0,mytime):
    print(x)
    for y in range(0,20):
        print(y,end="")
print(mytime)
for i in range(mytime,0,-1):
    seconds=i%60
    minutes=int(i/60)%60
    hours=int(i/3600)%60
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("gay")
print(mytime)