n=int(input())
temp=n 
sum=0
while(temp!=0):
    p=temp%10
    sum=(sum*10)+p 
    temp=temp//10
print(True if(n==sum) else False)
