
# coding: utf-8

# In[2]:

import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/")

c = r.content
soup = BeautifulSoup(c,"html.parser")


all = soup.find_all("div", {"class":"propertyRow"})


#all[0].find("h4",{"class":"propPrice"}).text.strip()

l=[]
for item in all:
    d={}
    d["Price"]=(item.find("h4",{"class":"propPrice"}).text.strip())
    d["Address"]=(item.find_all("span",{"class":"propAddressCollapse"})[0].text)
    d["Locality"]=(item.find_all("span",{"class":"propAddressCollapse"})[1].text)
    try:
        d["Beds"]=(item.find("span",{"class":"infoBed"}).find("b").text)
    except:
        d["Beds"]=(None)
    
    try:
        d["Area"]=(item.find("span",{"class":"infoSqFt"}).find("b").text)
    except:
        d["Area"]=(None)
    
    try:
        d["Full Bath"]=(item.find("span",{"class":"infoValueFullBath"}).find("b").text)
    except:
        d["Full Bath"]=(None)
        
    try:
        d["Half Bath"]=(item.find("span",{"class":"infoValueHalfBath"}).find("b").text)
    except:
        d["Half Bath"]=(None)
        
    for column_group in item.find_all("div", {"class":"columnGroup"}):
        #print(column_group)
        fG = column_group.find_all("span",{"class":"featureGroup"})
        fN = column_group.find_all("span",{"class":"featureName"})
        for feature_group, feature_name in zip(fG,fN):
            if "Lot Size" in feature_group.text:
                d["Lot Size"]=(feature_name.text)
    l.append(d)

    print(" ")
#print(l)
import pandas as pd
(pd.DataFrame(l))
#df=pd.DataFrame(l)

#df.to_csv("data.csv")

