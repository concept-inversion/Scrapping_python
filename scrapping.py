from bs4 import BeautifulSoup
import urllib.request
import pandas 
import numpy



url ="https://cdn.rawgit.com/younginnovations/internship-challenges/master/data-analysis/scrape-it/exampledata.html"
from urllib.request import urlopen
html = urlopen(url)
soup = BeautifulSoup(html)
print (soup.prettify())