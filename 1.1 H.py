import math as m
a=int(input("Введите а: "))
x=int(input("Введите x: "))
y=int(input("Введите y: "))
G=float
G=(m.sin(m.fabs(y+x))**3-(x+y))/((m.atan(x+a)**4)*(x**5))
print("G= ",G)
