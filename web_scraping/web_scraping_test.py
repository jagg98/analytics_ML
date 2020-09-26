from selenium import webdriver
from bs4 import BeautifulSoup
import lxml.html as lh
import pandas as pd
import requests


url = 'https://www.hispanosnba.com/equipos/atlanta-hawks/calendario/2019-20'
page = requests.get(url)
soup = BeautifulSoup(page.content, "lxml")
page1 = soup.find('div', {"class":"main block"})

page1 = page1.find('main', {"class":"content block"},)


titles = page1.findAll('section', {"class":"bordered block"})[0]
title = titles.find('div', {"class":"hlist"})
tabla = title.find('table', {"class":"tblcal"})
tr_elements = tabla.findAll(['tr'])
i = 0
col = []
for t in tr_elements[0]:
    i+=1
    name=t.text.strip()
    
    col.append((name,[]))

page1 = page1.findAll('section', {"class":"bordered block"})


for pageNumber in page1:
    classhlist = pageNumber.find('div', {"class":"hlist"})
    tabla = classhlist.find('table', {"class":"tblcal"})
    tr_elements = tabla.findAll(['tr'])
    i = 0
    for j in range(1,len(tr_elements)):
        element = tr_elements[j]
        i = 0
        for t in element:
            
            name  = t.text.strip()
            
            col[i][1].append(name)
            i+=1


#page1 = page1.find('div', class_ = 'hlist')
#page2 = lh.fromstring(page.content)
#tr_elements = page2.xpath('//tr')
#page1 = page1.findAll('tbody', {"class":""})
#page1 = page1.find('tr')
#page1 = page1.find('td', class_ = 'tdr')
#print([len(T) for T in tr_elements[:12]])

# i = 0
# col = []
# for t in tr_elements[0]:
#     i+=1
#     name=t.text.strip()
#     print(i,name)
#     col.append((name,[]))



# for j in range(1,len(tr_elements)):
#     element = tr_elements[j]
#     i = 0
#     for t in element:
        
#         name  = t.text.strip()
#         print(i,name)
#         col[i][1].append(name)
#         i+=1


dicc = {title:column for (title,column) in col}

df = pd.DataFrame(dicc)

# print(len(col))
print(df.head())
# for i in range(len(col)):
#     print(col[i][0])












