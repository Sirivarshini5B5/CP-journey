def str_len(string):
    l=list(string.split(" "))
    return len(l[-1])


t=int(input())
while(t>0):
    str=input()
    print(str_len(str))
    t=t-1
