n=int(input())
for row in range(1,n+1):
    for space in range(n,row,-1):
        print(" ",end="")
    for num in range(1,row+1):
        print(num,end="")
    for num1 in range(row-1,0,-1):
        print(num1,end="")
    print("")
