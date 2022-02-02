t=int(input())
for _ in range(t):
    x=input()
    y=input()
    c=0
    for i in range(len(x)):
        if x[i]==y[i]:
            c+=1
        elif x[i]=="?" or y[i]=="?":
            c+=1
        else:
            break
    if c==len(x):
        print("Yes")
    else:
        print("No")
