print("Поиск чисел из отрезка")
a=int(input("От: "))
b=int(input("До: "))
c=int(input("Которые дают остаток: "))
d=int(input("При делении на число: "))
if a<b:
    print("В отрезок входят числа: ")
    for i in range(a, b):
        if (i%d==c):
            print(i)
elif a>b:
    print("В отрезок входят числа: ")
    for i in range(b, a):
        if (i%d==c):
            print(i)
else:
    print("Нет таких чисел!")
