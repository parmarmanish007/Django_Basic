class arith():
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def add(self):
       return self.a+self.b

    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
c=arith(5,10)
print("add :",c.add())
print("sub :",c.sub())
print("mul :",c.mul())
