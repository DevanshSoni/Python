
# coding: utf-8
# In[13]:
from bs4 import BeautifulSoup
from urllib.request import urlopen
html=urlopen("https://www.sololearn.com")
soup=BeautifulSoup(html,"lxml")
title=soup.title    #getting title of the webpage
print(title)
# In[17]:
for i in soup.find_all("a", href=True):  
    if(i['href'][0]=='\'):
        continue
    else:  
        print(i["href"])      #getting all the links from the webpage
