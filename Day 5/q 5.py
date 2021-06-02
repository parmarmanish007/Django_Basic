class employee():
    def __init__(self):
        name=input("Enter a name :")
        desigation = input("Enter a position :")
class subclass(employee):
    def field(self):
        salary=int(input("Enter a salary :"))

c=subclass()
c.field()