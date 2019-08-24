n=int(input())
temp=n
am=0
while n!=0:
    rem=int(n%10)
    am=am+rem**3
    n=int(n/10)
if temp == am:
    print("yes")  
else:
    print("no")


