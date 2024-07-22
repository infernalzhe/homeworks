try:
    with open("input1.txt", "r") as file1:
        lines1 = file1.readlines()
    file1.close()
except FileNotFoundError:
    print("Net fila input1")
try:
    with open("input2.txt", "r") as file2:
        lines2 = file2.readlines()
    file2.close()
except FileNotFoundError:
    print("Net fila input2")
mfile1 = [0] * len(lines1)
mfile2 = [0] * len(lines2)
output = [0] * len(lines1)
for i in range(len(lines1)):
    mfile1[i] = lines1[i].strip()
for j in range(len(lines2)):
    mfile2[j] = lines2[j].strip()
print(f"{mfile1}\n{mfile2}")
for i in range(len(mfile1)):
    for j in range(i,len(mfile1)):
        if str(mfile1[i]) >= str(mfile1[j]):
            t = mfile1[i]
            mfile1[i] = mfile1[j]
            mfile1[j] = t
for i in range(len(mfile1)):
    output[i] = mfile1[i]
for i in range(len(mfile2)):
    for j in range(len(output)):
        try:
            if (str(output[j-1]) < str(mfile2[i])) and (str(mfile2[i]) < str(output[j])):
                output.insert(j,mfile2[i])
            elif str(mfile2[i]) > output[(len(output)-1)]:
                output.append(mfile2[i])
        except:
            continue
print(output)
with open("output.txt", "w") as out:
    for i in output:
        out.write(i + "\n")