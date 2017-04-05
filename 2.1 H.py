import math as m
x=float(input("Введите координату x: "))
y=float(input("Введите координату y: "))
if (x,y<=1 or x,y>=-1) and y>0:
    if ((x<=1 and x>0) or (x>=-1 and x<0)) and m.fabs(x)<=y:
        print("Точка входит в закрашенную область")
    else:
        print("Точка не входит в закрашенную область")
else:
    print("Точка не входит в закрашенную область")


    
