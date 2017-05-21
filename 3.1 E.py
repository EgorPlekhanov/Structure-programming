x=float(input("Введите X: "))
n=int(input("Введите N: "))
s=0
t=0
i=2
if n<=0:
        print("N<=0!!!")
else:
    for i in range(i,n+1):
        if i%2==0:
            t=-x*(2*i+1)/(2*i+1)
            s=s+t
        else:
            t=x*(2*i+1)/(2*i+1)
            s=s+t
    s=s+x
    print("Значение= ",s)
