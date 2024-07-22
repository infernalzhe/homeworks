def var(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return var(n-1) + var(n-2)
n = int(input("Vvedite kolichestvo stypenek n = "))
v = var(n)
print(f"variantov: {v}")
