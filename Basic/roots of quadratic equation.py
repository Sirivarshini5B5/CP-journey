import cmath
a,b,c=map(int,input().split())
d=(b**2)-(4*a*c)
r1=(-b+cmath.sqrt(d))/2*a
r2=(-b-cmath.sqrt(d))/2*a
print(r1,r2)
