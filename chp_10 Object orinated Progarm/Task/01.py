class programer:
    compny="Microsoft"
    # ye class attriutes he quki sabhi microsfot se belong karte he 
    def __init__(self,name,product):
        self.name=name
        self.product=product
        
    def print(self):
        print(f"Name of progarmer is {self.name} and product is {self.product}")


data=programer("Abrar", "bygus")
data.print()