import random

def gameWin(comp,you):
    # Givr a condtion 
    if(comp==you):
        return None
    elif(comp=="s"):
        if(you=="w"):
            return False
        elif(you=="g"):
            return True
    elif(comp=="w"):
        if(you=="g"):
            return False
        elif(you=="s"):
            return True
    elif(comp=="g"):
        if(you=="s"):
            return False
        elif(you=="w"):
            return True
    



print("computer  Turn : Snake(s) Water(w) or Gun(g)? : ")
# Take a random value 1 to 3
randno=random.randint(1,3)

# giving a condtion for computer
if (randno==1):
    comp="s"
elif (randno==2):
    comp="w"
else:
    comp="g"        

# get a choice form user
you = input("Your  Turn : Snake(s) Water(w) or Gun(g)? : ")

# store a function in a 
a=gameWin(comp,you)

print(f"Computer Chosse : {comp}\n\n")
print(f"Your are Chosse : {you}\n\n")


# give a condtion for win or lose
if (a==None):
    print("Game is Tie : \n\n")
elif a:
    print("You Are win : \n\n")
else:
    print("You Are lose : \n\n")   

