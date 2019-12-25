print("enter the range of number")
n=int(input())
f1=0
f2=1
print(f1)
print(f2)
while(n-2>0):
    a=f1+f2
    f1=f2
    f2=a
    print(a)
    n=n-1
    
