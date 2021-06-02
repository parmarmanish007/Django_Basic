class cal2():
    def setdata(self):
        self.radius=int(input("Enter a radius :"))

    def area(self):
        PI=3.142
        self.ans = PI*(self.radius*self.radius)

    def display(self):
        print(" area of circle is :",self.ans)

c=cal2()
c.setdata()
c.area()
c.display()