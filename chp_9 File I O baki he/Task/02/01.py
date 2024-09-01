def game():
    return 999

score=game()#contion a game function value in a score 

f=open("score.txt","r")
high=f.read()

if (high<score):
    f=open("score.txt","w")
    f.write(str(score))

