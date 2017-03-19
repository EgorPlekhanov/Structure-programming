x=int(input("Введите число x: "))
print ("Натуральные делители числа x: ")
for i in range(1,x):
    if (x%i == 0):
        print(i)
print(x)

