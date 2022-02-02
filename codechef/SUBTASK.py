t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split())
    l=list(map(int,input().split()))
    if l.count(1)==n:
        print("100")
    elif m==l[:m].count(1):
        print(k)
    else:
        print("0")
