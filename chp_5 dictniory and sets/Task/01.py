a={
    "pankha":"Fan",
    "Dabba":"Box ",
    "Chiz":"Item"
}
print(a.keys())

b=input("Enter a Key Name What You Want to Find : ")
print("Your word meaning is : ",a[b])
# .get line error nhi dega none dega
print(a.get(b))
