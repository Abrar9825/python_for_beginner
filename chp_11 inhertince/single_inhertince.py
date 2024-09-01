# parant class may attributes hona comulsory he 
class Employy:
    compny="Google"
    def getdet(self):
        print(f"This is Base Class Which Compny name is {self.compny}")

# child class may ager nhi hoga to vo parant may check kargea age rmil jata he to print kargea nhi to error dega 
class pro(Employy):
    compny="Micro"
    Language="python"
    # def getdet(self):
    #     print(f"This is child Class Which Compny name is {self.compny}")
    def lang(self):
        print(f"This is child Class Which Language name is {self.Language}")

# we are also overwrite on a base calss 
e=Employy()
p=pro()
# e.getdet()
p.getdet()
p.lang()