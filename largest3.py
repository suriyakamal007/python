n1,n2,n3=input().split()
n1=int(n1)
n2=int(n2)
n3=int(n3)
if ((n1>n2)and(n1>n3)):
    print(int(n1))
elif ((n2>n1)and(n2>n3)):
    print(int(n2))
else:
    print(int(n3))
