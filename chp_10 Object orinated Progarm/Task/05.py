class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getstus(self):
        print("*********************")
        print(f"Name of Train is {self.name} ")
        print(f"Sets are avalibale in a Train is {self.seats} ")
        print("*********************")

    def fareinfo(self):
        print(f"price of a tickte is {self.fare}")
        print("*********************")

    def bookticket(self):
        if(self.seats > 0):
            print(
                f"Ticket is booked in a :  {self.name} your seats number is  : {self.seats}")
                # jitne baar run karenge utne baar setes kam hojeyge
            self.seats = self.seats-1
        else:
            print("Train is full : ")


a = Train("Kach", 1900, 300)
a.getstus()
a.bookticket()
a.bookticket()

a.fareinfo()
