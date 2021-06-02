class publisher:
    def __init__(self,name):
        self.name=name
        print("name of the title :",self.name)
class book(publisher):
    def __init__(self,page):
        self.page=page
        print("page number: ",self.page)
class tape(publisher):
    def __init__(self,time):
        self.time=time
        print("time for playing :",self.time)

p=publisher("python")
b=book("10")
t=tape("1 hour")
