import pandas as pd
import csv

def csvStrtoList(csv_data):
    csv_data = str(csv_data)
    csv_data = csv_data.replace(' ', '')
    csv_data = csv_data.split(',')
    return csv_data
  
df = pd.read_csv("TemporaryRecommandIndie.csv", encoding='cp949')  

DayList = df['발매일']
TitleList = df['타이틀']
ArtistList = df['아티스트']
ProducerList = df['프로듀서']
ScoreList = df['점수']
TotalList = []

df2 = pd.read_csv('indieWD.csv', encoding='cp949')

ManList = df2['가수']
PeopleScoreList = df2['점수']

for i in range(0, len(TitleList)):
  tempArtist = csvStrtoList(ArtistList[i])
  tempProducer = csvStrtoList(ProducerList[i])
  
  tempList = []
  for man in tempArtist:
    tempList.append(man)
  for man in tempProducer:
    tempList.append(man)
  tempList = list(set(tempList))
  
  ScoreList[i] = 0
  
  for j in range(0, len(ManList)):
    for artist in tempList:
      if (ManList[j] == artist):
        ScoreList[i] += PeopleScoreList[j]
        continue
    
for i in range(0, len(ArtistList)):
  TotalList.append([DayList[i], TitleList[i], ArtistList[i], ProducerList[i], ScoreList[i]])
  
result = []

for i in TotalList:
  if (i[4] != 0):
    result.append(i)
  
with open('RecommandIndie.csv', 'w', encoding='CP949', newline='') as f:
  writer = csv.writer(f)
  writer.writerow(['발매일', '타이틀', '아티스트', '프로듀서', '점수'])
  writer.writerows(result)