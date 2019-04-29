# Python Program to Find LCM of two numbers

def lcm(a,b):
    if a>b:
        greater=a
    else:
        greater=b
    while(True):
        if((greater%a==0) and (greater%b==0)):
            lcm=greater
            break
        greater+=1
    return lcm
x=int(input("Enter first number:"))
y=int(input("Enter second number:"))
print("LCM of",x,"and",y,"is",lcm(x,y))
