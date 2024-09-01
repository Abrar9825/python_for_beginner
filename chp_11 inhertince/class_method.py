class home:
    member = 6
    name = "abrar"
    loction = "Mol's Ki pol : "

    # dender Class Alos known
    # def changeclass(self,sal):
    #     self.__class__.member=sal

    # second way
    @classmethod
    def change(cls, sal):
        cls.member = sal


obj = home()
print(obj.member)
obj.change(12)
print(obj.member)
