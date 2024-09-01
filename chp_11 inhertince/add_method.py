class Number:
    def __init__(self, num):
        self.num = num

    def __add__(self, num1):
        print("Add a Two Number : ")
        return self.num+num1.num


n1 = Number(4)
n2 = Number(6)
sum = n1+n2
print(sum)
