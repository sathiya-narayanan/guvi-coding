print("enter a number")
n=int(input())
count=1
for i in range(2,n):
    if(int(n%i)==0):
        count=0
    else:
        break
if(count==1):
    print("prime")
else:
    print("not prime")
