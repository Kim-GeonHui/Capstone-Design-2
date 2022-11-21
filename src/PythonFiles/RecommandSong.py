import pandas as pd
import csv

def csvStrtoList(csv_data):
    csv_data = csv_data.replace(' ', '')
    csv_data = csv_data.split(',')
    return csv_data
  
df = pd.read_csv("bugsdance2022.csv", encoding='cp949')  

ArtistList = df['아티스트']
ProducerList = df['프로듀서']
DayList = df['발매일']
TitleList = df['타이틀']
TotalList = [];

df2 = pd.read_csv('danceWD.csv', encoding='cp949')

ManList = df2['가수']
ScoreList = df2['점수']

for i in range(0, len(ArtistList)):
  TotalList.append([DayList[i], TitleList[i], ArtistList[i], ProducerList[i], 0])

for i in TotalList:
  tempTitle = csvStrtoList(i[2])
  for j in range(0, len(ManList)):
    for name in tempTitle:
      if (ManList[j] == name):
        i[4] += ScoreList[j]

result = []

for i in TotalList:
  if (i[4] != 0):
    result.append(i)

with open('TemporaryRecommandDance.csv', 'w', encoding='CP949', newline='') as f:
  writer = csv.writer(f)
  writer.writerow(['발매일', '타이틀', '아티스트', '프로듀서', '점수'])
  writer.writerows(result)