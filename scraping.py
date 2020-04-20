#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from bs4 import BeautifulSoup
import re
import requests
urls = ["https://www.yourdanishlife.dk/things-to-do/" , "https://www.yourdanishlife.dk/category/wine-dine/" , "https://www.yourdanishlife.dk/shopping-2/" , "https://www.yourdanishlife.dk/culture/" , "https://www.yourdanishlife.dk/category/living-here/" , "https://www.yourdanishlife.dk/category/living/christmas/" , "https://www.yourdanishlife.dk/category/shopping/food/" , "https://www.yourdanishlife.dk/travel-2/"]
# get website information
articles = []
for url in urls:
    r  = requests.get(url)
    data = r.text
    #soupify the data
    soup = BeautifulSoup(data, "html.parser")
    mydivs = soup.findAll("div", {"class": "block-grid-item"})
    links = []
    for article in mydivs:
        href_list = article.find_all("h3")
        for href in href_list:
            if article.find("a"):
                links.append(article.find("a")["href"])
    for link in links:
        article = requests.get(link)
        soup2 = BeautifulSoup(article.text, "html.parser")
        category = soup2.find("a", {"rel": "category"}).text
        headline = soup2.find("h1", {"class": "entry-title"}).text
        text = []
        for p_tag in soup2.findAll("p"):
            text.append(p_tag.text)
        cleaned_text = (" ").join(text[1:-3])
        temp_dict = {"category": category, "headline": headline, "text":cleaned_text}
        articles.append(temp_dict)
df = pd.DataFrame(articles)
df.to_csv("expats1.csv", sep=";")


# In[ ]:




