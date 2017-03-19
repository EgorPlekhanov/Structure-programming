x=float(input("Спортсмен пробежал в первый день (x): "))
y=float(input("Общее кол-во километров (y): "))
d=int(1)
while x<=y:
   x=x*0.1+x
   d=d+1
print("Номер дня: ",d)
