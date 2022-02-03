t=int(input())
for _ in range(t):
    s=input()
    s=list(s)
    if "1" not in s:
        print("NO")
    else:
        j=s.index("1")
        c=0
        for i in range(j,len(s)):
            if s[i]=="1":
                c+=1
            else:
                break
        if c==s.count("1"):
            print("YES")
        else:
            print("NO")
        
