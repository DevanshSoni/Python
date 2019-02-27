from bs4 import BeautifulSoup
from urllib.request import urlopen
req=urlopen("https://en.wikipedia.org/wiki/Machine_learning")
type(req)
soup=BeautifulSoup(req,"html5lib")
type(soup)
sub=soup.select(".mw-headline")
head=soup.select(".firstHeading")
for i in head:
    print(i.get_text())
for i in sub:
    print(i.get_text())