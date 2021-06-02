class cal6():
    def setdata(self):
        self.lenght=int(input("Enter a lenght :"))
    def display(self):
        area =self.lenght*self.lenght
        print("area of {} is :".format(self.lenght),area)
c=cal6()
c.setdata()
c.display()