# ginving a argu in a function
def max(num1,num2,num3):
    
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3

a=int(input("Enter a Value : "))
b=int(input("Enter a Value : "))
c=int(input("Enter a Value : "))
# put a varible in a function calling
m=max(a,b,c)

print("is the max value : ",str(m))