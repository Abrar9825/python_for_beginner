a = int(input("Enter Your Marks :  "))

if(a < 50):
    print("Your Grade is F ")
elif(a > 50 and a < 60):
    print("Your Grade is D")
elif(a > 60 and a < 70):
    print("Your Grade is C")
elif(a > 70 and a < 80):
    print("Your Grade is B")
elif(a > 80 and a < 90):
    print("Your Grade is A")
elif(a > 90 and a < 100):
    print("Your Grade is Exllant")
else:
    print("Not Valid Marks : ")
