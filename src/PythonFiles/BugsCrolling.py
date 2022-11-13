from lib2to3.pgen2 import driver
import selenium
from selenium import webdriver as wd
import time
import pandas as pd
from bs4 import BeautifulSoup
import requests
from itertools import repeat
import csv
import math
import re

title_list = []
singer_list = []

for i in range(1,131):
  
  driver = wd.Chrome('C:\chromedriver')
  driver.maximize_window()

  url = 'https://music.bugs.co.kr/newest/track/nrh?page=%d'%i
  h = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'}
  driver.get(url)

  html = driver.page_source 
  soup = BeautifulSoup(html, 'html.parser')

  title = soup.select('tbody tr th p.title a')
  singer = soup.select('tbody tr td.left p.artist a')

  isTrue = False;
  
  for j in title:  
    j = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z&!?$@()+-=.':;<>/*^%#_\s]", "", j.text);
    j = j.replace(u'\xa0',u'')
    title_list.append(j)
    
  for j in singer:
    if (j.text[0] == '\n'):
        continue;
    j = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z&!?$@()+-=.':;<>/*^%#_\s]", "", j.text);
    j = j.replace(u'\xa0',u'')
    singer_list.append(j)
    
  driver.close()
  driver.quit()

total_list = []
for j in range(6500):
  total_list.append([title_list[j], singer_list[j]]);

with open('hiphoptest.csv', 'w', encoding='CP949', newline='') as f:
  writer = csv.writer(f)
  writer.writerow(['타이틀', '아티스트'])
  writer.writerows(total_list)