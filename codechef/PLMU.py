t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    c1=l.count(2)
    c2=l.count(0)
    print((c1*(c1-1)//2)+c2*(c2-1)//2)
