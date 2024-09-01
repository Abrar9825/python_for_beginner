class Employye():
    # ye auto run karega khud ku 
    def __init__(self,name,age,salary):
        # stroe a argu in a same name 
        self.name=name
        self.age=age
        self.salary=salary
        print(f"Auto run : ")

    # print data which is we are storee
    def printdata(self):
        print(f"Name of Empoloyee is :  {self.name}")
        print(f"age of Empoloyee is :  {self.age}")
        print(f"salary of Empoloyee is :  {self.salary}")


# ye object ko ential karta he or sirf comare karate he ye run hojyega 
run=Employye("Abrar",18, 100000)
run.printdata()