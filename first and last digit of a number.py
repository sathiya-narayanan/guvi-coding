print("enter the digit")
n=int(input())
ld=n%10
while(n>10):
    n=n//10
print("the first digit is",n,"the last digit is",ld)
