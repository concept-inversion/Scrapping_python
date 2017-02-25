from bs4 import BeautifulSoup
import requests
import csv
url ="https://cdn.rawgit.com/younginnovations/internship-challenges/master/data-analysis/scrape-it/exampledata.html"
page = requests.get(url)
print(page.status_code)
better = BeautifulSoup(page.content,'html.parser')

table = better.find('tbody')

for row in table.findAll('tr'):
    cells=[]
    for cell in row.findAll('td'):
        text=cell.text
        cells.append(text)
        print(cells)
