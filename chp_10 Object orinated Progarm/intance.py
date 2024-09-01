class add:
    salary = 300


# object
abrar = add()
maaz = add()

# when we don't write a instance then it's contion a class value which we are define
abrar.salary = "100"
print(abrar.salary)
# pele ye intance may dekhega ke value heke nhi ager use value nhi milte he to dyrek class lo contion kar lega
print(maaz.salary)
