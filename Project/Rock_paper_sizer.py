import random

def gamewin(comp,you):
    # contion a same value
    if(comp==you):
        return None
# when comouter chosse a Rock
    elif(comp=="r"):
        if(you=="p"):
            return True
        elif(you=="s"):
            return False
# when comouter chosse a Rock
    elif(comp=="p"):
        if(you=="s"):
            return True
        elif(you=="r"):
            return False
# when comouter chosse a Rock
    elif(comp=="s"):
        if(you=="r"):
            return True
        elif(you=="p"):
            return False                



print("Compuer Turn : Rock(r) pepar(p) scissors(s) : ")

random=random.randint(1, 3)

if (random==1):
    comp="r"
elif(random==2):
    comp="p"
else :
    comp="s"

you=input("Your Turn : Rock(r) pepar(p) scissors(s) : ")
# First value leke he function declare karne ka hamesha 
a=gamewin(comp,you)

print("You chosse  : ",you)
print("comp chosse  : ",comp)

if(a==None):
    print("Game is Tie")
elif a:
    print("You are win : ")
else:
    print("You are lose : ")


