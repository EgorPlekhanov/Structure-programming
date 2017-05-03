n=5
m=10
a=[]
b=[]
maxim=0
for i in range(n):
    a.append([])
    for j in range(m):
        print("Введите элемент ",i+1," строки, ",j+1," столбца:")
        a[i].append(int(input()))
        if abs(a[i][j])>maxim:
            maxim=abs(a[i][j])
print("Исходный массив: ",a)
print("Максимальный элемент по модулю = ",maxim)
for i in range(n):
    b.append([])
    for j in range(m):
        b[i].append(a[i][j]/maxim)
print("Второй массив: ",b)
