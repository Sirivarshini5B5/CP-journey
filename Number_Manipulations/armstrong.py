n=int(input())
sum=0
temp=n
while(temp>0):
    p=temp%10
    sum=sum+(p**3)
    temp=temp//10
print(True if(n==sum) else False)
