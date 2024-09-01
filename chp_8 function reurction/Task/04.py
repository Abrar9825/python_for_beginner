n=int(input("Enter a Number : "))

def rec(n):
    fact=1
    for i in range(1,n):
        fact=rec(n-1)+n
    return fact    

print("sum of natural number is : ",rec(n))
