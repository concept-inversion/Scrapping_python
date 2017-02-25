from bs4 import BeautifulSoup
import requests
import csv
import os
print(os.getcwd())
url ="https://cdn.rawgit.com/younginnovations/internship-challenges/master/data-analysis/scrape-it/exampledata.html"
page = requests.get(url)
print(page.status_code)
better = BeautifulSoup(page.content,'html.parser')

table = better.find('tbody')

rows=[]
for row in table.findAll('tr'):
    cells=[]
    for cell in row.findAll('td'):
        text=cell.text
        cells.append(text)
    rows.append(cells)

if (os.path.isdir('./out')==False):
    os.mkdir ("/out")
os.chdir ("out")
outputfile = open('./test.csv','w',newline='', encoding='utf8')
writer = csv.writer(outputfile)
writer.writerows(rows)
