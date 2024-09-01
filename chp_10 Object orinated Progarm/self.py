class Employye:
    def umar(self):
        print(f"Age is {self.age}")
        print(f"Age is {self.age}")


abrar=Employye()
Maaz=Employye()

abrar.age=45
Maaz.age=35

abrar.umar()
Maaz.umar()


# it's really Work like That 
# Employye.umar(abrar)

# first abrar function is run and then it's gone so conduct a 2 print msg which is self so it's print a 2 time same argument
# -----output----
# Age is 45
# Age is 45
# Age is 35
# Age is 35