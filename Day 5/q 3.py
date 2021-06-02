class cal3():
    def __init__(self):
        self.p=int(input("Enter a Principal amount :"))
        self.r=int(input("Enter a rate :"))
        self.n=int(input("Enter a time :"))
    def callinterest(self):
        self.ans=self.p*self.r*self.n/100
    def display(self):
        print("Simple interest is :",self.ans)

a=cal3()
a.callinterest()
a.display()