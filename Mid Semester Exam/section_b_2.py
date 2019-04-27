# Question 2-a

X=10
Y=10
A=20
B=A
print(id(A)==id(B))
A=A+1
print(id(A)==id(Y))

# Question 2-b
# Write a Python program to that takes as input total marks of students out of 500 and calculate the grade of students,
# if marks>=80%, grade is O
# if marks>=70% and <80%, grade is A+
# if marks>=60% and <70%, grade is A
# if marks<60%, grade is P

marks=int(input("Enter total marks out of 500: ")) 
grade=(marks/500)*100
if marks>500:
    print("Invalid range, enter marks again")
elif grade>=80:
    print("For",marks,"obtained, grade is O")
elif grade>=70 and grade<80:
    print("For",marks,"obtained, grade is A+")
elif grade>60 and grade<70:
    print("For",marks,"obtained, grade is A")
elif grade<60:
    print("For",marks,"obtained, grade is P")

# Question 2-c
# Write a function to find LCM of two numbers and use this function to find LCM of two inputs

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