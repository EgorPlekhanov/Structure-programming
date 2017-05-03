n=12
a=[float(input("Введите элемент массива ")) for i in range(n)]
a.sort(reverse=True)
s=max(a)+min(a)
print("Элементы в порядке убывания: ",a)
print("Сумма максимального и минимального элементов= ",s)
