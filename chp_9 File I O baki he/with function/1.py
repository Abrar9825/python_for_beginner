with open("1.txt","r") as f:
    a=f.read()

with open("1.txt","w") as f:
    a=f.write("Hello")
print(a) 

# in  With function we are not close a file adn continus work for another mode
# When we write a any kind of text in file consol give lenghth of string 