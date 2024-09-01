num=int(input("Enter a Number : "))
prime=True
for i in range(2,num):
    if (num%i==0):
        prime=False
        break
if prime==True:
    print(num," : is a prime Number : ")   
else:
    print(num," : is a not prime Number : ")    
