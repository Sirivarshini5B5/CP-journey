t=int(input())
for _ in range(t):
    n=int(input())
    c=0
    while(n>0):
        if n>=100:
            c+=n//100
            n=n%100
        elif n>=50 and n<100:
            c+=n//50
            n=n%50
        elif n>=10 and n<50:
            c+=n//10
            n=n%10
        elif n>=5 and n<10:
            c+=n//5
            n=n%5
        elif n>=2 and n<5:
            c+=n//2
            n=n%2
        elif n==1:
            c+=n//1
            n=n%1
    print(c)
            
