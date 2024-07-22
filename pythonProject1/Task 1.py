slo = {
}
cit = []
pop = []
count = 0
while True:
    try:
        n = int(input("Vvedite population: "))
        break
    except ValueError:
        print("try again")
        continue
try:
    with open("cities.txt", "r") as cities:
        lines = cities.readlines()
        cit = [0] * len(lines)
        pop = [0] * len(lines)
    cities.close()
except FileNotFoundError:
    print("Fila ne vizhy")
print(lines)
for i in lines:
    line = i.split(":")
    if int(line[1]) >= n:
        cit[count] = line[0].strip()
        pop[count] = line[1].strip()
    count += 1
print(cit, pop)
for i in range(len(cit)):
    for j in range(i, len(cit)):
        if str(cit[i]) >= str(cit[j]):
            t = cit[i]
            cit[i] = cit[j]
            cit[j] = t
            p = pop[i]
            pop[i] = pop[j]
            pop[j] = p
print("sorted")
print(cit, pop)
for i in range(len(cit)):
    slo[cit[i]] = pop[i]
if 0 in slo:
   del slo[0]
print(slo)
with open("filtered_cities.txt", "w") as out:
    for key, value in slo.items():
       out.write(f"{key}: {value}\n")