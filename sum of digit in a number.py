print("enter the digit")
n=int(input())
i=0
count=0
while(n>0):
    a=n%10
    i=a+i
    n=n//10
print("the sum of the digits is",int(i))

    
