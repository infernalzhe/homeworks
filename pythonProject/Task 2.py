ed = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
des = ["десять", "двадцвать", "тридцать", "сорок", "пятьдясят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
sot = ["сто", "двести","триста","четыресто", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
os = ["одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семьнадцать", "восемнадцать", "девятнадцать"]
number = input("Введите число от 1 до 999: ")
if len(number) == 3:
    a = number[0]
    b = number[1]
    c = number[2]
    if b == "1":
        print(f"{sot[int(a)-1]} {os[int(c)-1]}")
    else:
        print(f"{sot[int(a)-1]} {des[int(b)-1]} {ed[int(c)-1]}")
elif len(number) == 2:
    b = number[0]
    c = number[1]
    if b == "1":
        print(f"{os[int(c)-1]}")
    else:
        print(f"{des[int(b)-1]} {ed[int(c)-1]}")
elif len(number) == 1:
    c = number[0]
    print(f"{ed[int(c) - 1]}")