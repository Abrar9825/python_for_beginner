a1=int(input("Enter a first number : "))
a2=int(input("Enter a Secind number : "))
a3=int(input("Enter a Third number : "))
a4=int(input("Enter a Fourth number : "))

if(a1>a2 and a1>a3 and a1>a4):
    print(a1,"is Greter then ",a2,a3,a4)
elif(a2>a1 and a2>a3 and a2>a4):
    print(a2,"is greter then ",a1,a3,a4)
elif(a3>a1 and a3>a2 and a3>a4):
    print(a3,"is greter then ",a1,a2,a4)
else:
    print(a4,"is Gretar Then ",a1,a2,a3)