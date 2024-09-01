class dada:
    name="Yusuf"
    def grand(self):
        print("Hello I am Grand Father : ")

class Abba(dada):
    age=56
    def Baap(self):
        print("Hello I am Baap : ")

class Beta(Abba):
    loction="Mol ki pol"
    def Bacha(self):
        print("Hello I am Bacha : ")


d=dada()
a=Abba()
b=Beta()

b.Bacha()
print(b.name)


