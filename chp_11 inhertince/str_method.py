class Number:
    def __init__(self,num):
        self.num=num
    def __str__(self):
        return f"This is Number of  : {self.num}"

n=Number(9)
print(n)