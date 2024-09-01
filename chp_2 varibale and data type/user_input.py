a = input("Enter Your Name : ")
b = input("Enter Your Name : ")

# the input Box Always Contions a String Format
# When We Want a Do Some Arurthmatic opration then We Are use a Type casting (is possible)
print("type of a ", type(a))
print("type of b ", type(b))


print("string Addtion  is : ", a+b)
# it's give a Output in a string format
# now We Are using a typecasting
a = int(a)
b = int(b)


print("type of a ", type(a))
print("type of b ", type(b))

print("Now The addtion of int Value is ", a+b)
