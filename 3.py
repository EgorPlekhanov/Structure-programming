a=int(input("Введите число a: "))
b=int(input("Введите число b: "))
c=int(input("Введите число c: "))
if (a+b>c) and (a+c>b) and (b+c>a):
    print("Треугольник с данными сторонами существует.")
else:
    print("Треугольника с данными сторонами не существует.")

