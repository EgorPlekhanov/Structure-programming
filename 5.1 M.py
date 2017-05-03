n=12
i=1
a=[float(input("Введите элемент массива ")) for i in range(n)]
s=1
t=0
while s<n:
    for i in range(n-s):
        if a[i]<a[i+1]:
            t=t+1
            a[i],a[i+1]=a[i+1],a[i]
    s+=1      
print("Элементы в порядке убывания: ",a)
print("Количество перестановок: ",t)
