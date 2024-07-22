count = 0
sum = 0
outmarks = []
outnames = []
try:
   with open('input.txt','r') as text:
      lines = text.readlines()
      marks = [0] * len(lines)
      names = [0] * len(lines)
   text.close()
   for j in lines:
      line = j.split(',')
      marks[count] = line[1].strip()
      names[count] = line[0].strip()
      count += 1
   for i in range(len(marks)):
      sum = int(marks[i]) + sum
   avg = sum / len(marks)
   for i in range(len(marks)):
      if int(marks[i]) > avg:
         outmarks.append(marks[i])
         outnames.append(names[i])
   total = [0] * len(outmarks)
   for i in range(len(outmarks)):
      total[i] = outnames[i] + ", " + outmarks[i]
   print(f"file na vixod {total}")
   with open("output.txt", 'w') as output:
      for i in total:
         output.write(i + "\n")
except FileNotFoundError:
   print('Fila ne vizhy')