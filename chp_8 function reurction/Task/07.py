# strip is remove a spaces
# hello="   Abrar      "
# hello1="  Abrar   "
# print(hello)
# print(hello1.strip())


def remover_sprit(string,word):
    newstr=string.replace(word,"")
    return newstr.strip()

this="  Abrar Shaikh is  here ?    "
n=remover_sprit(this, "Shaikh")
print(n)
