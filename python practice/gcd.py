def gcd_cal(a,b):
    if(a>b):
        small=b
    else:
        small=a
    for i in range(1,small+1):
        if((a%i==0) and (b%i==0)):
            gcd=i
        
    return gcd

t=int(input())
while(t>0):
    a,b=map(int,input().split())
    print(gcd_cal(a,b))
    t=t-1
