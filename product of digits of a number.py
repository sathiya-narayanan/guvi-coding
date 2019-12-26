print("enter a number")
n=int(input())
p=1
while(n>1):
    l=n%10
    p=p*int(l)
    n=n/10
print("the product of the digits of the number is",p)
