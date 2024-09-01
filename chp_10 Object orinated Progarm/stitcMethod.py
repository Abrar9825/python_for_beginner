class greet:
    # Here we write a multiple argu what we can show in terminal
    def salary(self,argu):
        print(f"salary is : {self.pagar} : {argu}")

    @staticmethod
    def good():
        print("Good night : ")


# Store a class
Total=greet()
# Store a Value in a attributes 
Total.pagar=20000
# calling a function
Total.salary("Thanks : ")
# and calling a good function with static method
Total.good()

