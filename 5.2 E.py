n=int(input("Введите N "))
m=int(input("Введите M "))
a=[]
p=0
for i in range(n):
    a.append([])
    for j in range(m):
        print("Введите элемент ",i+1," строки, ",j+1," столбца:")
        a[i].append(int(input()))
        if a[i][j]==7:
            p=p+1
if p>0:
    print("Семёрка встречается ",p," раз(а).")
else:
    print("Семёрки в массиве нет.")
