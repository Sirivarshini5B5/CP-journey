t=int(input())
for i in range(t):
    s=input()
    if(s=="b" or s=="B"):
        print("BattleShip")
    elif(s=="c" or s=="C"):
        print("Cruiser")
    elif(s=="d" or s=="D"):
        print("Destroyer")
    elif(s=="f" or s=="F"):
        print("Frigate")
