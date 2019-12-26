def fact(l):
    r=l+1
    y=1
    for i in range(1,r):
        y=y*i
    return y
    
print("enter a number")
n=int(input())
z=n
s=0
while(n>1):
    l=n%10
    s=s+fact(int(l))
    n=n/10

print(s)
if(s==z):
    print("the number is strong number")

else:
    print("the number is not a strong number")
