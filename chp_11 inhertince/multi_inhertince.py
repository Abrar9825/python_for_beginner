class father:
    name = "Aarif"
    age = 0

    def umar(self):
        self.age = self.age+1


class after1yr:
    name="abrar"


class child(father, after1yr):
    name="Maaz"


obj = child()
obj.umar()
print(obj.age)
print(obj.name)
