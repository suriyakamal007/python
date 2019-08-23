
"""
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

n=int(input())
print(fact(n))
"""
count=1
n=int(input())
for i in range(1,n+1):
    count*=i
print(count)
