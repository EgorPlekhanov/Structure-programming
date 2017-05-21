a=bool([-5,...,5])
i=int
i=int(input("Введите число: "))
if -5<=i<=5:
    a[i]=true
while i!=0:
    i=int(input("Введите число: "))
    if -5<=i<=5:
        a[i]=true
if a==null:
    print("Чисел нет!")
else:
    for i in range(11):
        if a[i]:
            print("Числа лежащие в интервале от -5 до 5:",a,' ')
