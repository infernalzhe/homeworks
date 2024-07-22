def evk(a,b):
    if a > b:
        n = a % b
        if n == 0:
            return b
        return evk(n,b)
    else:
        n = b % a
        if n == 0:
            return a
        return evk(a,n)
a = int(input("Vvedite pervoe 4islo a =  "))
b = int(input("Vvedite vtoroe 4islo b =  "))
n = evk(a,b)
print(f"a = {a}, b = {b}, NOD = {n}")