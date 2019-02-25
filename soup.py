
# coding: utf-8

# In[13]:


from bs4 import BeautifulSoup
from urllib.request import urlopen
html=urlopen("https://www.sololearn.com")
soup=BeautifulSoup(html,"lxml")
title=soup.title
print(title)


# In[17]:


a=soup.find_all("a")
for i in a:
    print(i.get("href"))


# In[19]:


# for getting all "a" tags
a=soup.find_all
soup.find_all("a")


# In[39]:


html=urlopen("https://www.tutorialspoint.com/html/html_tables.htm")
soup=BeautifulSoup(html,"lxml")
head=soup.find_all("li")
print(head[10])

