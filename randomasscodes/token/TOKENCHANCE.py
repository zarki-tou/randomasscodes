import random
jacks=0
Ls=0
for x in range(0,1000):
    for a in range(0,100):
        ta=random.randrange(68750)
        if ta==68750:
            print(ta,end="")
            print("jackpot")
            jacks+=1
        else:
            print(ta)
            Ls+=1
print(f"L:{Ls} Tokens:{jacks}")
if jacks:   
    print(f"U GOT {jacks} A TOKEN")