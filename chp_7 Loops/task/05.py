num=int(input("Enter a number : "))
sum=0
if (num<0):
    print("Number is not valid : ")
else :    
    for i in range(1,num+1):
        sum=sum +i
    print(sum)