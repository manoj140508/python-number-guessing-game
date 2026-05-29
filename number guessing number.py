# number guessing game

a=32
b=47
c=58
d=79
print("we have four different numbers between 1 to 100 as a,b,c,d")
z=input("choose a number(a,b,c,d):")
if z=="a":
    num=a
elif z=="b":
    num=b
elif z=="c":
    num=c
elif z=="d":
    num=d
else:
    print("invalid input")
    exit()

attempts=0

while True:
    guess=int(input("what's your guess:"))
    attempts +=1

    if abs(guess - num) <= 5 and guess != num:
        print("Very close!")
    
    elif guess>num:
        print("lower than your guess")
    elif guess<num:
        print("higher than your guess")
    else:
        print("you are correct")
        print("u guessed it in:",attempts,"attempts")
        break 



         

    
