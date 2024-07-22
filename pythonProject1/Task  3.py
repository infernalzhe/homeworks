a = str(input("Vvedite nazvanie coursa (Math/History/Science/Art): "))
try:
    with open("input.txt", "r") as file:
        lines = file.readlines()
        names = [0] * len(lines)
        subj = [0] * len(lines)
    file.close()
except FileNotFoundError:
    print("Fila ne vizhy")
for i in range(len(lines)):
    line = lines[i].split(":")
    names[i] = line[0].strip()
    subj[i] = line[1].strip()
for j in range(len(subj)):
    if a in subj[j]:
        print(names[j])