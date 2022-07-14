def add(a,b):
    res=a+b
    return res
def sub(a,b):
    res=a-b
    return res
def multi(a,b):
    res=a*b
    return res
def div(a,b):
    res=a//b
    return res

val1=int(input("enter a first number:--"))
val2=int(input("enter a second number:--"))
u=int(input('''what u want:--           
1.Addition
2.Substraction
3.Multiplication
4.Division

'''))

if u==1:
    d=add(val1,val2)
    print("Addition:--",d)
elif u==2:
    d=sub(val1,val2)
    print("sub:--",d)
elif u==3:
    d=multi(val1,val2)
    print("multi:--",d)
elif u==4:
    d=div(val1,val2)
    print("div:--",d)