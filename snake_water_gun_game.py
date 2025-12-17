import random

computer=random.choice([-1,0,1])
yourstr=input("Enter your choice : ")

dt={"s":1,"w":0,"g":-1}
rev_dt={1:"snake",0:"water",-1:"gun"}
yournum=dt[yourstr]

print(f"computer choose {rev_dt[computer]} and you choose {rev_dt[yournum]}")
print("Welcome guys, To the snake water and gun game")

if(computer==yournum):
    print("Match Withdraw")
else:
    if(computer==-1 and yournum==1):
        print("you loose ! ")    
    elif(computer==-1 and yournum==0):
        print("you win , yeeeyyyy")    
    elif(computer==0 and yournum==1):
        print("you win , ohhho")
    elif(computer==0 and yournum==-1):
        print("you loose , oppps")  
    elif(computer==1 and yournum==0):
        print("you loose")   
    elif(computer==1 and yournum==-1):
        print("you win")      
