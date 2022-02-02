t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ma=max(a)
    mi=min(a)
    print(ma-mi)
