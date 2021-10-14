n=int(input())
flag=0
for i in range(n):
    if(2**i==n):
        flag=flag+1
if(flag==1):
    print("true")
else:
    print("false")
