#defult argument
def sum(a = 6,b = 8):
    print(a * b)
sum(8,9),sum()
#keyword argument
def sum(a,b):
    print("sum is :",a + b)
sum(b = 10,a = 20)
#variable lenght argument
def add(*num):
    sum = 0
    for i in num:
        sum = sum + i
    print("sum :",sum)
add(10,20)
add(10,20,30)
# variable key word aragument
def my_func(**num):
    for i ,j in num.items():
        print(i,j)
my_func(name='parmar',lastname='manish')