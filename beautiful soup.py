from bs4 import BeautifulSoup
from urllib.request import urlopen
html=urlopen("https://www.sololearn.com")
soup=BeautifulSoup(html,"lxml")
title=soup.title
print(title)
a=[1,2,3]
a.