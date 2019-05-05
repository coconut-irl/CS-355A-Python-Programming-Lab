# Python Program to Display Fibonacci sequence Using Recursion
def gen_seq(length):
    if(length <= 1):
        return length
    else:
        return (gen_seq(length-1) + gen_seq(length-2))
length = int(input("Enter number of terms:"))
print("Fibonacci sequence using Recursion :")
for iter in range(length):
    print(gen_seq(iter))