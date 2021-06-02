class cal5():
    def __init__(self):
        self.width=int(input("Enter a width :"))
        self.height=int(input("Enter a height :"))
    def calArea(self):
        self.area=self.width*self.height

    def display(self):
        print("Area of rectangle is :",self.area)
c=cal5()
c.calArea()
c.display()