st1=str(input("Введите строку 1: "))
st2=str(input("Введите строку 2: "))
n=len(st1)
m=len(st2)
i=1
j=1
st3=''
if n>=m:
    for i in range(n):
        for j in range(m):
            if st1[i]==st2[j]:
                st3+=st1[i]
    if st3=="":
        print("Нет совпадений")
    else:
        print("Строка, состоящая из символов, которые входят в обе строки:",st3)
else:
    for j in range(m):
        for i in range(n):
            if st1[i]==st2[j]:
                st3+=st1[i]
    if st3=="":
        print("Нет совпадений")
    else:
        print("Строка, состоящая из символов, которые входят в обе строки:",st3)

