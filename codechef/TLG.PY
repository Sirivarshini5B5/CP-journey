t=int(input())
diff=0
s1=0
s2=0
lead=0
for i in range(t):
    a,b=map(int,input().split())
    s1+=a
    s2+=b
    if(s1>s2):
        diff=s1-s2
        if(diff>lead):
            lead=diff
            winner=1
    elif(s2>s1):
        diff=s2-s1
        if(diff>lead):
            lead=diff
            winner=2
            
print(winner,lead)
