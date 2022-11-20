import csv
 
arr1 = []
arr2 = []
tempIndex = 0
 
f = open('2019IndieWDEC.csv', 'r', encoding='cp949')
rdr = csv.reader(f)
for line in rdr:
  if (line[3] == 'Weighted Degree'):
    continue
  arr1.append(line[1])
  arr2.append(float(line[3]) * 0.2)
f.close()

f = open('2020IndieWDEC.csv', 'r', encoding='cp949')
rdr = csv.reader(f)
for line in rdr:
  if (line[3] == 'Weighted Degree'):
    continue
  
  if line[1] in arr1:
    tempIndex = arr1.index(line[1])
    arr2[tempIndex] += float(line[3]) * 0.3
  else:
    arr1.append(line[1])
    arr2.append(float(line[3]) * 0.3)
f.close()

f = open('2021IndieWDEC.csv', 'r', encoding='cp949')
rdr = csv.reader(f)
for line in rdr:
  if (line[3] == 'Weighted Degree'):
    continue
  
  if line[1] in arr1:
    tempIndex = arr1.index(line[1])
    arr2[tempIndex] += float(line[3]) * 0.5
  else:
    arr1.append(line[1])
    arr2.append(float(line[3]) * 0.5)
f.close()

total_list = []
for j in range (0, len(arr1)):
  total_list.append([arr1[j], arr2[j]])

with open('indieWD.csv', 'w', encoding='CP949', newline='') as f:
  writer = csv.writer(f)
  writer.writerow(['가수', '점수'])
  writer.writerows(total_list)