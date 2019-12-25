print("enter a number")
n=int(input())
s=0
while(n!=0):
    a=n%10
    s=s*10+a
    n=n//10
if(n==s):
    print("the given number is palindrome")

else:
    print("not a palindrome number")
    
