import time
import random 

mytime=int(input("enter ur time: "))
ta=random.random()
for i in range(mytime,0,-1):
    seconds=i%60
    minutes=int(i/60)%60
    hours=int(i/3600)%24
    days=int(i/86400)%7
    weeks=int(i/604800)%4
    monts=int(i/2628000000)%12
    year=int(i/31540000000)
    print(f"{year}:{monts}:{weeks}:{days}:{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)
print("gay")
print(f"segundos:{mytime}")
##print(ta)
##print(round(ta,2))