a=''' Dear Name
    You are selected
    date
'''
name=input("Enter Your Name : \n")
date=input("Enter a Date : \n")
a= a.replace("Name", name)
a= a.replace("date", date)
print(a)

