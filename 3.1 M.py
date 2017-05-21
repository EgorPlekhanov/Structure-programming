k=int(input("Введите k: "))
x=float
y=0
r=1
for i in range(1,k+1):
    if (i!=3):
        x=(-1**i)/((i-3)**2)
        y=y+x
    for n in range(i,2*k+1):
        if n!=2:
            t=(n**3-8)/(n+2)
            r=r*t
w=y*r
print("w=",w)
    
