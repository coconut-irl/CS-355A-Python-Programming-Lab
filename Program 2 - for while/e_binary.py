# Python Program to convert binary number to decimal number

def fun(n):
    return int(n,2)
num=int(input("Enter a binary number:"))
print("Decimal conversion of",num,"is",fun(num))