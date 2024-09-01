# normal find persnatge
# marks1=[23,45,24,90,28]
# persnatge=(sum(marks1)/500)*100
# print(persnatge)

# function contion a sum of value and return a andswer
# sun is pre define keyword

# without argu

# def per():
#     ans=(sum(marks)/400)*100
#     return ans


# marks=[11,22,33,44]
# persant1=per()
# print(persant1)

# marks=[99,88,77,64]
# persant2=per()
# print(persant2)




# with argu
# with argu may esa hota he ke def per may jo varible asign he vo  he define hoga
# jese marks1 ke value aayegi to uska varible leke ayega 
def per(marks):
    ans=(sum(marks)/400)*100
    return ans


marks1=[11,22,33,44]
persant1=per(marks1)
print(persant1)

marks2=[99,88,77,64]
persant2=per(marks2)
print(persant2)

