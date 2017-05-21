n=float(input("Введите n: "))
m=float(input("Введите m: "))
if 1<=n<=1000:
    p=n**2-2*n*m+m**2
    print("Квадрат разности n и m =",p)
else:
    print("Число n не находится в промежутке от 1 до 1000")
