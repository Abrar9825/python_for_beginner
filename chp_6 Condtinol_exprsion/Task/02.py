a1=int(input("Enter a C++ Marks : "))
a2=int(input("Enter a HTML Marks : "))
a3=int(input("Enter a python Marks : "))

sum=a1+a2+a3
sum=sum/300*100

if(sum<33):
    print("You are a fail Your Persatnge is : ",sum)
else:
    print("You are pass Your persantge is : ",sum)
