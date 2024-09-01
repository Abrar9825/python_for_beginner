# Main parant
class dada:
    name = "Yusuf"

    def grandFather(self):
        print("I am Your Grand Faher : ")

    def age(self):
        print("My age is 89 : ")

# Second parant

class father(dada):
    # name = "Aarif"

    def abba(self):
        print("I Your Father : ")

    def age(self):
        print("My age is 59 : ")

#Child 

class son(father):
    # name = "abrar"

    def beta(self):
        print("I am Son : ")

    # def age(self):
    #     print("My age is 19 : ")


d = dada()
f = father()
s = son()

s.age()
print(s.name)

# jab hum child se condtion call karate he to vo total jitne bhi parants he vo sab ka data apne ander le  leleta he 
# or ager parnts se karate he to vo uske upper vale parnts ka sab data lega nake child ka 
# or ager main parnst se karta ahe to vo sirf apna he data access karge niche ke koi bhi child ka data access nhi karega 


