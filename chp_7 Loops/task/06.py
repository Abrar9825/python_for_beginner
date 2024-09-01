# n!=n X n X n X
# 5!=5*4*3*2*1
num=int(input("Enter a number : "))
fact=1
# yaha +1 iske liye use kiya he quki hue main value tak cahiye 
for i in range(1,num+1):
    fact=fact*i
print(f"Factorial of {num} is {fact} ")