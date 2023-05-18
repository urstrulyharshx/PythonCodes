class programmer():
    company="microsoft"
    def __init__(self,name,product):
        self.name=name
        self.product=product
    def getinfo(self):
        print(F"The name of the {self.company} programmeris {self.name} and product is {self.product}")
harsh=programmer("Harsh","Github")
harsh.getinfo()