# Python Program to Find the Sum of Digits in a Number

num=int(input("Enter a number:"))
sum=0
while(num>0):
    reminder=num%10
    sum=sum+reminder
    num=num//10
print("Sum of the digits of the given number:",sum)