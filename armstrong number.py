print("enter a number")
n=int(input())
r=n
i=0
while(n>0):
    a=n%10
    i=i+a**3
    n=n//10

if(i==r):
    print("the number is armstrong number")

else:
    print("not a palindrome")
