#funaction with return
def disp(name):
    return name
name = disp("manish")
print(name)

def show():
    name = "parmar manish"
    contact = 9714241051
    return name,contact
name,contact = show()
print("Name is",name)
print("contact number is",contact)