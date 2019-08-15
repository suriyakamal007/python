n1,n2=input().split()
n1=int(n1)
n2=int(n2)-1
while((n1<n2) and (n1!=n2)):
    n1=n1+1
    if(int(n1%2)==0):
        print(n1, end=" ")
    
