class employee:
    salary=300
    bonus=200
    # totalsalary=500
    @property
    def totalsalary(self):
        return self.salary+self.bonus

    
    @totalsalary.setter
    def totalsalary(self,val):
        self.bonus =val -self.salary
        

# when we are using a property then it's bheve like a property not a like function\
# And it's aslo known as getter property
e=employee()
print(e.totalsalary)            
e.totalsalary=1000
print(e.salary)
print(e.bonus)  
