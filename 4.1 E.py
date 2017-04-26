t=str(input("Введите строку: "))
i=1
n=len(t)
s=0
for i in range (0,n):
    p=ord(t[i])
    s=s+p
print("Сумма кодов всех символов заданной строки= ",s)
