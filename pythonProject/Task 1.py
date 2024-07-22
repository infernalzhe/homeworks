i = 1
b = "*"
N = int(input("Введите N (нечетное целое число): "))
while i <= N:
    spacenum = int((N-i)/2)
    zv = b * i
    print(f"{" " * spacenum}{zv}{" " * spacenum}")
    i = i + 2