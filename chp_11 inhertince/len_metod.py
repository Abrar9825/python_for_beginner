class Number:
    def __init__(self,num):
        self.num=num
      
    def __len__(self):
        return 1

n=Number(7)
print(len(n))
# it's return a value of length of number which we are return