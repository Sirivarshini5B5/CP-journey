t=int(input())
while(t>0):
    a=int(input())
    x=round(a**(1/3))
    y=x*x*x
    if(a==y):
        print("YES")
    else:
        print("NO")
    t=t-1