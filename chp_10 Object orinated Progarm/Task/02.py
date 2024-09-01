class cal:
    def __init__(self, num):
        self.num = num

    def cube(self):
        print(f"Cube of {self.num} is {self.num **2}")

    def squre(self):
        print(f"Cube of {self.num} is {self.num **3}")
        

    def rootsqure(self):
        print(f"Cube of {self.num} is {self.num **0.5}")
        


ans = cal(3)
ans.cube()
ans.squre()
ans.rootsqure()
