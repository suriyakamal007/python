num=int(input())
cal=int(num/2)
count=0
for i in range(1,cal):
    if num/i==0:
        count+=1
if count==2:
    print("no")
else:
    print("yes")
    
