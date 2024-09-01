f=open("1.txt","r")
t=f.read()
if "Abrar" in t:
    print("Abrar is here : ")
else:
    print( "Abrar is Not here :  ")    
f.close()