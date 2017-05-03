n=int(input("Введите количество элементов в массиве: "))
i=1
a=[input("Введите элемент массива ") for i in range(n)]
s=1
a1=-1
a2=-1
r=0
while s<n:
   for i in range(n-s):
       if a[i]==a[n-s]:
           p=a[i]
           a1=i
           a2=n-s
           r=r+1
   s+=1
if r>1:
    print("Больше двух одинаковых элементов!")
elif a1!=-1 and a2!=-1:
    print("Индексы одинаковых элементов: ",a1," и ",a2,", элементы = ",p)
else:
    print("Нет совпадений!")
