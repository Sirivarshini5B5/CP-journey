t=int(input())
for _ in range(t):
    r=int(input())
    x1,x2=map(int,input().split())
    y1,y2=map(int,input().split())
    z1,z2=map(int,input().split())
    xy=((x1-y1)**2)+((x2-y2)**2)
    yz=((y1-z1)**2)+((y2-z2)**2)
    xz=((x1-z1)**2)+((z2-x2)**2)
    if xy<=(r**2) and yz<=(r**2) and xz<=(r**2):
        print("yes")
    elif xy<=(r**2) and yz<=(r**2) or xz<=(r**2):
        print("yes")
    else:
        print("no")
