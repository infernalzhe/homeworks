num = (input("Введите число: "))
summ = 0
for i in num:
    summ = summ + int(i)
num = str(summ)
while summ >= 10:
    print(summ)
    summ = 0
    for i in num:
        summ = summ + int(i)
    num = str(summ)
print(summ)