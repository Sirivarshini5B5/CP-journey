t=int(input())
for _ in range(t):
    n=int(input())
    k=0
    c=0
    for i in range(1,n+1):
        k+=i
        if k<=n:
            c+=1
        else:
            break
    print(c)
