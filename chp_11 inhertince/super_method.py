# Jab May esa chata hu ke mere ander jo function he vo to run he ho baki mere parnt may bhi ager ye vala function he to vo bhi run ho
# so then i use a super() key

# Main parant
class dada:
    name = "Yusuf"

    def grandFather(self):
        print("I am Your Grand Faher : ")

    def age(self):
        print("My age is 89 : ")

# Second parant

class father(dada):
    name = "Aarif"

    def abba(self):
        print("I Your Father : ")

    def age(self):
        super().age()
        print("My age is 59 : ")

#Child 

class son(father):
    name = "abrar"

    def beta(self):
        print("I am Son : ")

    def age(self):
        super().age()
        print("My age is 19 : ")


d = dada()
f = father()
s = son()

# d.age()
# here i am not a print a father age but i use a super key then is take same function in A parnts 
# f.age()
s.age()


# jab hum child se condtion call karate he to vo total jitne bhi parants he vo sab ka data apne ander le  leleta he 
# or ager parnts se karate he to vo uske upper vale parnts ka sab data lega nake child ka 
# or ager main parnst se karta ahe to vo sirf apna he data access karge niche ke koi bhi child ka data access nhi karega 


